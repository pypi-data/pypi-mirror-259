import pandas as pd
import numpy as np
import os
import json
from typing import *

from .data.preprocess import *
from .data.archive import *
from .analysis.cluster import *
from .analysis.optimization import *
from .analysis.outlier_detection import *
from .visualization.graph import *


# CALLER FUNCTIONS HERE


'''
Processing Functions
'''


def run_sentence_transform(
        csv_path: Optional[str] = None,
        device: str = 'cpu',
        load_path: Optional[str] = None,
        archive_path: Optional[str] = None
) -> np.ndarray:
    """
    Performs sentence-level semantic similarity analysis on data from a CSV file.

    Args:
        csv_path (str): Path to the CSV file containing the data.
            Required headers: 'SERNUM','PCA','CPN_1','DateCode_1','LOTCODE_1','MPN_1','RD_1', 'HWRMA'.
        device (str): Device to use for sentence transformation. Defaults to 'cpu'.
        load_path (Optional[str]): Path to a NumPy file containing archived
            data to load instead of preprocessing.
        archive_path (Optional[str]): Path to a NumPy file where the
            transformed data will be archived.

    Raises:
        FileNotFoundError: If the CSV file or load path is not found,
            or if the directory for the archive path does not exist.
        PermissionError: If there is no write access to the directory
            for the archive path.
        ValueError: If an invalid device is used for sentence transformation
            or the CSV file does not contain the required headers.

    Returns:
        np.ndarray: NumPy array containing the transformed sentence embeddings.
    """
    # Load data based on provided path or preprocess the data
    if not load_path:
        
        # Check if the CSV path points to a valid file
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file '{csv_path}' not found.")
        
        # Accepted device types
        accepted_devices = ['cpu', 'cuda', 'ipu', 'xpu', 'mkldnn', 'opengl', 'opencl', 'ideep', 'hip', 've', 'fpga', 'ort',
                            'xla', 'lazy', 'vulkan', 'mps', 'meta', 'hpu', 'mtia', 'privateuseone']

        # Check if the provided device is in the accepted list
        if device not in accepted_devices:
            raise ValueError(f"Invalid device type '{device}'. Accepted device types are: {', '.join(accepted_devices)}")
    
        data = preprocess(csv_path)
        st_data = sentence_transform(data, device)
    else:
        if not isinstance(load_path, str):
            raise ValueError("Input 'load_path' must be a string representing the file path if provided.")

        if not os.path.exists(load_path):
            raise FileNotFoundError(f"File at load path '{load_path}' not found.")
        st_data = np.load(load_path)

    if archive_path:
        # Check if archive_path exists and if its directory is writable if provided
        archive_np_data(archive_path, st_data)

    return st_data


def run_dimension_reduction(
        table: Union[pd.DataFrame, str],
        st_embeddings: Union[np.ndarray, str],
        param_dict: Union[str, Dict[str, Union[int, float]]],
        seed: int = 42,
        archive_path: Optional[str] = None
) -> pd.DataFrame:
    """
    Performs dimensionality reduction on sentence embeddings and appends the reduced dimensions to a table.

    Args:
        table (Union[pd.DataFrame, str]): Either a Pandas DataFrame containing the data
            or a string representing the path to a CSV file containing the data.
        st_embeddings (Union[np.ndarray, str]): Either a NumPy array of sentence embeddings
            or a string representing the path to a NumPy file containing the embeddings.
        param_dict (Dict[str, Union[int, float]]): A dictionary containing the parameters
            for the dimension reduction algorithm.
        seed (int, optional): Random seed for reproducibility. Defaults to 42.
        archive_path (str, optional): Path to a CSV file where the resulting table will be archived.

    Returns:
        pd.DataFrame: The original table with two additional columns: 'DATA_X' and 'DATA_Y'
            containing the reduced dimensions.

    Raises:
        ValueError: If the inputs are not of the expected types.
        FileNotFoundError: If the archive path directory does not exist.
        PermissionError: If there is no write access to the archive path directory.
    """

    # Load the table if a path is provided
    table = to_dataframe(table)

    # If st_embeddings is a string, assume it's a path and load the object
    st_embeddings = to_ndarray(st_embeddings)

    # Check if param_dict is a dictionary
    param_dict = to_dict(param_dict)

    # Ensure seed is a positive integer
    if not isinstance(seed, int) or seed <= 0:
        raise ValueError("Input 'seed' must be a positive integer.")

    umap_data = dimension_reduction(st_embeddings, param_dict, seed)

    table = table.assign(DATA_X=umap_data[:, 0])\
                 .assign(DATA_Y=umap_data[:, 1])

    # Check if archive_path exists and if its directory is writable if provided
    if archive_path:
        archive_pd_data(archive_path, table)

    return table


def run_clustering(
        table: Union[pd.DataFrame, str],
        param_dict: Union[str, Dict[str, Union[int, float]]],
        archive_path: Optional[str] = None,
) -> pd.DataFrame:
    """
    Performs clustering on dimensionally reduced data and appends the cluster labels to a table.

    Args:
        table (Union[pd.DataFrame, str]): Either a Pandas DataFrame containing the data
            or a string representing the path to a CSV file containing the data.
        param_dict (Dict[str, Union[int, float]]): A dictionary containing the parameters for the clustering algorithm.
        archive_path (str, optional): Path to a CSV file where the resulting table will be archived.

    Returns:
        pd.DataFrame: The original table with an additional column 'CLUSTERS' containing the assigned cluster labels.

    Raises:
        ValueError: If the inputs are not of the expected types.
        FileNotFoundError: If the archive path directory does not exist.
        PermissionError: If there is no write access to the archive path directory.
        IOError: If the required columns are not present in the table.
    """
    table = to_dataframe(table)

    try:
        _ = table[['DATA_X', 'DATA_Y']]
    except AttributeError:
        raise IOError("UMAP Data must be a columns in 'table'\n"
                        "Call 'run_dimension_reduction' before using this function")

    umap_data = np.array(list(zip(table['DATA_X'], table['DATA_Y'])))

    # Check if param_dict is a dictionary
    param_dict = to_dict(param_dict)

    labels = clustering(umap_data, param_dict)

    table = table.assign(CLUSTERS=labels)

    if archive_path:
        archive_pd_data(archive_path, table)

    return table


def run_optimizer(
        st_data: Union[np.ndarray, str],
        seed: int = 42,
        trials: int = 50,
        archive_path: Optional[str] = None
) -> Dict[str, Union[int, float]]:
    """
    Performs hyperparameter optimization for a model using sentence embeddings.

    Args:
        st_data (Union[np.ndarray, str]): Either a NumPy array of sentence embeddings
            or a string representing the path to a NumPy file containing the embeddings.
        seed (int, optional): Random seed for reproducibility. Defaults to 42.
        trials (int, optional): Number of optimization trials to run. Defaults to 50.
        archive_path (str, optional): Path to a NumPy file where the optimized parameters will be archived.

    Returns:
        Dict[str, Union[int, float]]: A dictionary containing the optimized hyperparameters.

    Raises:
        ValueError: If the inputs are not of the expected types.
        FileNotFoundError: If the archive path directory does not exist.
        PermissionError: If there is no write access to the archive path directory.
    """

    # checks if st_data is a path to a ndarray and retrieves it
    st_data = to_ndarray(st_data)

    # Ensure seed is an integer
    if not isinstance(seed, int) or seed <= 0:
        raise ValueError("Input 'seed' must be a positive integer.")
    
    # Ensure trials is a positive integer
    if not isinstance(trials, int) or trials <= 0:
        raise ValueError("Input 'trials' must be a positive integer.")
    
    # Perform optimization
    optimized_params = optimize_hyperparameters(st_data, seed, trials)

    # Save optimized results if archive_path is provided
    if archive_path:
        archive_dict(archive_path, optimized_params)

    return optimized_params


'''
Analysis Functions
'''


# modifies the original dataset to include
# cluster and outlier labels
def report_outliers(
        table: Union[pd.DataFrame, str],
        archive_path: Optional[str] = None
) -> pd.DataFrame:

    """
    Calculates outlier density for each cluster in a table and appends it as a new column.

    Args:
        table (pd.DataFrame): Pandas DataFrame containing cluster labels in a column named 'CLUSTERS'
            and outlier indicators in a column named 'HWRMA'.
        archive_path (str, optional): Path to a CSV file where the resulting table will be archived.

    Returns:
        pd.DataFrame: The original table with an additional column 'OUTLIER_DENSITY' containing
            the calculated outlier density for each cluster.

    Raises:
        ValueError: If the inputs are not of the expected types.
        FileNotFoundError: If the archive path directory does not exist.
        PermissionError: If there is no write access to the archive path directory.
        IOError: If the 'CLUSTERS' column is not present in the table.
    """

    # Check if table is a DataFrame or a string representing the file path
    table = to_dataframe(table)

    # Check if 'CLUSTERS' column exists
    if 'CLUSTERS' not in table.columns:
        raise IOError("Cluster Labels must be a column in 'table'. Call 'run_clustering' before using this function.")

	# Calculate outlier density for each cluster
    # for each cluster:
    # find the ratio of Trues to Falses in the HWRMA column
    # that ratio is the density of outliers in that group
    # save that value in the table
    unique_labels = table['CLUSTERS'].drop_duplicates().to_numpy()
    for label in unique_labels:
        hwrma_column = table.loc[table.CLUSTERS == label, "HWRMA"]
        outlier_ratio = hwrma_column.value_counts(normalize=True).get(True, 0)
        table.loc[table.CLUSTERS == label, 'OUTLIER_DENSITY'] = outlier_ratio

	# Save results to archive path if provided
    if archive_path:
        archive_pd_data(archive_path, table)

    return table


# takes the dataset and a number of clusters as input
# outputs a dataframe containing all the components unique to those clusters
# "num_clusters" can at most be the total number of clusters in the dataset
def suspect_components(
        table: Union[pd.DataFrame, str],
        num_clusters: int,
        archive_path: Optional[str] = None
) -> pd.DataFrame:

    """
    Identifies potential component suspects based on cluster analysis and outlier density.

    Args:
        table (pd.DataFrame): Pandas DataFrame containing:
            - A column named 'CLUSTERS' with cluster labels.
            - A column named 'OUTLIER_DENSITY' calculated by `report_outliers`.
            - Any additional component information used for grouping by `group_components`.
        num_clusters (int): Maximum number of clusters to consider as potential sources of suspects.
        archive_path (str, optional): Path to a CSV file where the identified suspects will be archived.

    Returns:
        pd.DataFrame: A DataFrame containing potential suspects, identified as components
            in clusters with high outlier density and not present in clusters with lower density.

    Raises:
        ValueError: If `num_clusters` is less than 1 or greater than the number of unique clusters.
            or the inputs are not of the expected types.
        FileNotFoundError: If the archive path directory does not exist.
        PermissionError: If there is no write access to the archive path directory.
        IOError: If required columns ('CLUSTERS', 'OUTLIER_DENSITY') are missing in the table.
    """


	# Check if table is a DataFrame or a string representing the file path
    table = to_dataframe(table)
    
    # Check if 'CLUSTERS' and 'OUTLIER_DENSITY' columns exist
    required_columns = ['CLUSTERS', 'OUTLIER_DENSITY']
    if not all(col in table.columns for col in required_columns):
        raise IOError("Required columns ('CLUSTERS', 'OUTLIER_DENSITY') are missing in the table. Check that you are providing report_outliers output")

    # Check if num_clusters is at least 1
    if num_clusters < 1:
        raise ValueError("Input 'num_clusters' must be at least 1.")
    
    # sort the table so the cluster with the highest outlier density is at the top
    table = table.copy(deep=True).sort_values(by=['OUTLIER_DENSITY'], ascending=False)

    # create a list of all the unique cluster labels
    labels = table['CLUSTERS'].drop_duplicates().to_numpy()

    cluster_limit = min(len(labels), num_clusters)

    # outliers are the components from the cluster with the highest error rate
    outliers = group_components(table, labels[:cluster_limit]).drop_duplicates(ignore_index=True)
    # inliers are the components from all other clusters
    inliers = group_components(table, labels[cluster_limit:]).drop_duplicates(ignore_index=True)

    # unique contains the components from outliers that are not also in inliers
    unique = outliers.merge(inliers, how='left', indicator='set')
    unique = unique[unique.set == 'left_only']
    unique = unique.drop(['set'], axis=1)

    # archive them to a csv
    if archive_path:
        archive_pd_data(archive_path, unique)

    return unique


# returns the row from the table with a given serial number
def find_sernum(
        sernum: str,
        table: Union[pd.DataFrame, str],
		archive_path: Optional[str] = None
) -> pd.DataFrame:

    """
    Finds the row in the table with a specified serial number.

    Args:
        sernum (str): The serial number to search for.
        table (pd.DataFrame): The DataFrame to search within.

    Returns:
        pd.DataFrame: A DataFrame containing the row with the matching serial number,
            or an empty DataFrame if no match is found.

    Raises:
        ValueError: If the inputs are not of the expected types.
    """

    # Check if sernum is a non-empty string
    if not isinstance(sernum, str) or not sernum:
        raise ValueError("Input 'sernum' must be a non-empty string.")

    # Check if table is a DataFrame or a string representing the file path
    table = to_dataframe(table)
    
    # Filter table for entry
    entry = table.loc[table['SERNUM'] == sernum]
    
	# Check if the entry was found
    if entry.empty:
        raise ValueError(f"No entry found for serial number '{sernum}'.")
    
	# Check if archive_path exists and if its directory is writable if provided
    if archive_path:
        archive_pd_data(archive_path, entry)
    
    return entry


# returns all rows from the table with a given cluster label
def find_cluster(
        cluster: int,
        table: Union[pd.DataFrame, str],
        archive_path: Optional[str] = None
) -> pd.DataFrame:

    """
    Finds all rows in the table with a specified cluster label.

    Args:
        cluster (int): The cluster label to filter by.
        table (pd.DataFrame): The DataFrame to search within.

    Returns:
        pd.DataFrame: A DataFrame containing all rows with the matching cluster label.

    Raises:
        ValueError: If the inputs are not of the expected types.
    """
    
	# Check if table is a DataFrame or a string representing the file path
    table = to_dataframe(table)
    
	# Filter table for entry
    entry = table.loc[table['CLUSTERS'] == cluster]
    
	# Check if the entry was found
    if entry.empty:
        raise ValueError(f"No entry found for cluster '{cluster}'.")
    
	# Check if archive_path exists and if its directory is writable if provided
    if archive_path:
        archive_pd_data(archive_path, entry)
    
    return entry


# returns all rows from the table matching the cluster label for a serial number
def find_cluster_by_unit(
        sernum: str,
        table: Union[pd.DataFrame, str],
        archive_path: Optional[str] = None
) -> pd.DataFrame:

    """
    Finds all rows in the table that belong to the same cluster as a specified serial number.

    Args:
        sernum (str): The serial number to identify the cluster.
        table (pd.DataFrame): The DataFrame to search within.

    Returns:
        pd.DataFrame: A DataFrame containing all rows belonging to the same cluster as the specified serial number.

    Raises:
        ValueError: If the inputs are not of the expected types.
    """
    # Check if sernum is a non-empty string
    if not isinstance(sernum, str) or not sernum:
        raise ValueError("Input 'sernum' must be a non-empty string.")

    # Check if table is a DataFrame or a string representing the file path
    table = to_dataframe(table)
    
    cluster_label = table.loc[table['SERNUM'] == sernum]['CLUSTERS'][0]

	# Filter table for entry
    entries = table.loc[table['CLUSTERS'] == cluster_label]
    
	# Check if the entry was found
    if entries.empty:
        raise ValueError(f"Cluster label '{cluster_label}' not found.")
    
	# Check if archive_path exists and if its directory is writable if provided
    if archive_path:
        archive_pd_data(archive_path, entries)
    
    return entries


# get the n best neighbors in the dimension-reduced set, based on distance
def find_neighbors(
        sernum: str,
        table: pd.DataFrame,
        n_neighbors: int,
        archive_path: Optional[str] = None
) -> pd.DataFrame:

    """
    Finds the n closest neighbors to a specified serial number in the dimension-reduced space.

    Args:
        sernum (str): The serial number to find neighbors for.
        table (pd.DataFrame): The DataFrame containing dimensionally reduced data.
        n_neighbors (int): The number of neighbors to retrieve.

    Returns:
        pd.DataFrame: A DataFrame containing the num closest neighbors to the specified serial number.

    Raises:
        ValueError: If the inputs are not of the expected types or n_neighbors < 0
    """

    # Check if num is at least 0
    if n_neighbors < 0:
        raise ValueError("Input 'num' must be at least 0.")

    # Check if table is a DataFrame or a string representing the file path
    table = to_dataframe(table)
    
    ref = find_sernum(sernum, table)
    try:
        _ = table[['DISTANCE']]
    except KeyError:
        table = table.assign(DISTANCE = lambda part : np.sqrt(pow(part.DATA_X - ref.DATA_X, 2) + pow(part.DATA_Y - ref.DATA_Y, 2)))
    table.sort_values(by='DISTANCE')
	
	# Filter table for neighbors
    neighbors = table[:n_neighbors]
    
	# Check if the neighbors were found
    if neighbors.empty:
        raise ValueError(f"Neighbors '{neighbors}' not found.")
    
	# Check if archive_path exists and if its directory is writable if provided
    if archive_path:
        archive_pd_data(archive_path, neighbors)
    
    return neighbors


def filter_for_anomalies(
        table: Union[pd.DataFrame, str],
        archive_path: Optional[str] = None
) -> pd.DataFrame:

    """
    Filters a dataset to include only rows marked as anomalies.

    Args:
        table (Union[pd.DataFrame, str]): Either a Pandas DataFrame containing the data
            or a string representing the path to a CSV file containing the data.

    Returns:
        pd.DataFrame: A DataFrame containing only the rows where the 'HWRMA' column is True,
            indicating known anomalies.

    Raises:
        ValueError: If the input is the wrong type or missing necessary columns.
    """

    table = to_dataframe(table)

	# Filter table for anomalies
    anomalies = table.loc[table['HWRMA'] == True]
    
	# Check if the anomalies were found
    if anomalies.empty:
        raise ValueError(f"Anomalies '{anomalies}' not found.")
    
	# Check if archive_path exists and if its directory is writable if provided
    if archive_path:
        archive_pd_data(archive_path, anomalies)
    
    return anomalies

# returns the row from the table with a given serial number
def filter_by_column(
        column_filter: List[str],
        table: pd.DataFrame,
        archive_path: Optional[str] = None
) -> pd.DataFrame:

    """
    Filters input digest to list only the specified properties for each part

    Args:
        column_filter (List[str]): The columns that must persist after culling.
        table (pd.DataFrame): The DataFrame to filter.
        archive_path (str, optional): Path to a CSV file where the filtered DataFrame will be archived.

    Returns:
        pd.DataFrame: A DataFrame containing filtered part data for each part in the input set.

    Raises:
        ValueError: If the inputs are not of the expected types or if the column_filter contains non-existent columns.
        FileNotFoundError: If the directory for the archive file does not exist.
        PermissionError: If there is no write access to the archive path directory.
    """

    # Check if table is a DataFrame or a string representing the file path
    table = to_dataframe(table)

    # Check if columns_filter is a non-empty list of strings
    if not isinstance(column_filter, list) or not all(isinstance(col, str) for col in column_filter):
        raise ValueError("Input 'column_filter' must be a non-empty list of strings.")

    # Check if columns in column_filter exist in the table
    missing_columns = [col for col in column_filter if col not in table.columns]
    if missing_columns:
        raise ValueError(f"Column(s) {', '.join(missing_columns)} do(es) not exist in the table.")

    # Filter table for specified part properties
    filtered_table = table.drop(columns=column_filter, inplace=False)

    # Archive the filtered DataFrame to a CSV file if archive_path is provided
    if archive_path:
        archive_pd_data(archive_path, filtered_table)

    return filtered_table

'''
Graphing Functions
'''


def plot_clusters(
        table: Union[pd.DataFrame, str],
        archive_path: Optional[str] = None
) -> None:

    """
    Generates a plot of data points colored by their cluster labels.

    Args:
        table (pd.DataFrame): A DataFrame containing columns named 'DATA_X', 'DATA_Y', and 'CLUSTERS',
            representing the dimensionally reduced data and cluster assignments.
        archive_path (str, optional): Path to a file where an image of the plot will be archived.

    Raises:
        ValueError: If the input is the wrong type
        IOError: If the required columns are not present in the table.
    """
    table = to_dataframe(table)

    try:
        _ = table[['DATA_X', 'DATA_Y', 'CLUSTERS']]
    except AttributeError:
        raise IOError("Cluster Labels and UMAP Data must be a columns in 'table'\n"
					  "Call 'run_dimension_reduction' and 'run_clustering' before using this function")

    points = np.array(list(zip(table['DATA_X'], table['DATA_Y'])))

    labels = table['CLUSTERS']

    plot_labeled_data(points, labels, "BoM Clusters", archive_path)
    

def plot_hwrma(
    table: Union[pd.DataFrame, str],
    archive_path: Optional[str] = None
) -> None:

    """
    Generates a plot of data points colored by their HWRMA (anomaly) status.

    Args:
        table (pd.DataFrame): A DataFrame containing columns named 'DATA_X', 'DATA_Y', and 'HWRMA',
            representing the dimensionally reduced data and HWRMA labels.
        archive_path (str, optional): Path to a file where an image of the plot will be archived.


    Raises:
        ValueError: If the input is the wrong type
        IOError: If the required columns are not present in the table.
    """

    table = to_dataframe(table)

    try:
        _ = table[['DATA_X', 'DATA_Y', 'HWRMA']]
    except AttributeError:
        raise IOError("Input 'table' must have 'HWRMA' column and UMAP Data.\n"
                      "Call 'run_dimension_reduction' before using this function")
    
    points = np.array(list(zip(table['DATA_X'], table['DATA_Y'])))
    labels = table['HWRMA']
    plot_labeled_data(points, labels, "BoM HWRMA labels", archive_path)


'''
Util Functions
'''

def to_ndarray(
        np_data: Union[str, np.ndarray]
) -> np.ndarray:
    """
    Ensures that the input is a NumPy array, either by loading it from a file or
    directly using the provided array.

    Args:
        np_data (Union[str, np.ndarray]): A NumPy array or a string representing the path to a NumPy array file.

    Returns:
        np.ndarray: The NumPy array.

    Raises:
        ValueError: If the input is not a NumPy array or a string representing a file path.
    """

    if isinstance(np_data, str):
        # Load the array if a path is provided
        np_data = np.load(np_data)
    elif isinstance(np_data, np.ndarray):
        np_data = np_data
    else:
        raise ValueError("Input must be a NumPy array or a string representing the file path.")

    return np_data


def to_dataframe(
        pd_data: Union[str, pd.DataFrame]
) -> pd.DataFrame:
    """
    Ensures that the input is a pandas DataFrame, either by loading it from a CSV file or
    directly using the provided DataFrame.

    Args:
        pd_data (Union[str, pd.DataFrame]): A pandas DataFrame or a string representing the path to a CSV file.

    Returns:
        pd.DataFrame: The pandas DataFrame.

    Raises:
        ValueError: If the input is not a pandas DataFrame or a string representing a file path.
    """

    if isinstance(pd_data, str):
        # Load the table if a path is provided
        pd_data = pd.read_csv(pd_data, header=0, low_memory=False)
    elif not isinstance(pd_data, pd.DataFrame):
        raise ValueError("Input must be a Pandas DataFrame or a string representing the file path.")

    return pd_data

def to_dict(
        dict_data: Union[str, Dict]
) -> pd.DataFrame:
    """
    Ensures that the input is a pandas DataFrame, either by loading it from a CSV file or
    directly using the provided DataFrame.

    Args:
        pd_data (Union[str, pd.DataFrame]): A pandas DataFrame or a string representing the path to a CSV file.

    Returns:
        pd.DataFrame: The pandas DataFrame.

    Raises:
        ValueError: If the input is not a pandas DataFrame or a string representing a file path.
    """

    if isinstance(dict_data, str):
        # Load the table if a path is provided
        with open(dict_data, 'r') as dict_file:
            dict_data = json.load(dict_file)

    elif not isinstance(dict_data, dict):
        raise ValueError("Input must be a Dictionary or a string representing the file path.")

    return dict_data

def combine_boms(
        bom_path_1: str,
        bom_path_2: str,
        archive_path: str
) -> pd.DataFrame:
    """
    Combines two CSV files containing bill of materials (BOMs) into a single DataFrame.

    Args:
        bom_path_1 (str): The path to the first BOM CSV file.
        bom_path_2 (str): The path to the second BOM CSV file.
        archive_path (str, optional): The path to save the combined BOM data. Defaults to None.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the combined BOM data.

    Raises:
        FileNotFoundError: If either of the specified CSV files does not exist.
        ValueError: If either of the CSV files does not contain the required headers.
    """

    # Check if the CSV paths point to valid files
    if not os.path.exists(bom_path_1):
        raise FileNotFoundError(f"CSV file '{bom_path_1}' not found.")
    
    if not os.path.exists(bom_path_2):
        raise FileNotFoundError(f"CSV file '{bom_path_2}' not found.")
    

    # Check if CSV files contain the appropriate headers
    for path, description in [(bom_path_1, "First BOM file"), (bom_path_2, "Second BOM file")]:
        try:
            _ = pd.read_csv(path, header=0, usecols=['SERNUM'])
        except KeyError:
            raise ValueError(f"CSV file '{path}' does not contain the required headers: ['SERNUM']")

    # Read both CSV files and concatenate them
    combined_data = pd.concat([pd.read_csv(bom_path_1), pd.read_csv(bom_path_2)])
    
    # Save combined data to archive_path if provided
    if archive_path:
        archive_pd_data(archive_path, combined_data)
    
    return combined_data
