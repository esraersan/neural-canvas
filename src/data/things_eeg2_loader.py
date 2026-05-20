import numpy as np
from pathlib import Path


def load_things_eeg2(data_dir: str, split: str = 'train') -> dict:
    """
    Load THINGS-EEG2 preprocessed data.

    Parameters
    ----------
    data_dir : str
        Path to the tutorial_data/eeg_dataset directory
    split : str
        'train' or 'test'

    Returns
    -------
    dict with keys:
        'eeg'    : np.ndarray — EEG data
        'times'  : np.ndarray — timepoints in seconds
        'channels': list — channel names
    """
    data_dir = Path(data_dir)

    if split == 'train':
        eeg = np.load(data_dir / 'preprocessed_eeg_training.npy',
                      allow_pickle=True).item()
    else:
        eeg = np.load(data_dir / 'preprocessed_eeg_test.npy',
                      allow_pickle=True).item()

    return {
        'eeg': eeg['preprocessed_eeg_data'],
        'times': eeg['times'],
        'channels': eeg['ch_names']
    }


def average_repetitions(eeg_data: np.ndarray) -> np.ndarray:
    """
    Average across repetitions to get stable responses.

    Parameters
    ----------
    eeg_data : np.ndarray
        Shape (conditions, repetitions, channels, timepoints)

    Returns
    -------
    np.ndarray
        Shape (conditions, channels, timepoints)
    """
    return eeg_data.mean(axis=1)


def baseline_correct(eeg_data: np.ndarray,
                     times: np.ndarray) -> np.ndarray:
    """
    Subtract pre-stimulus baseline (-200ms to 0ms).

    Parameters
    ----------
    eeg_data : np.ndarray
        Shape (conditions, channels, timepoints)
    times : np.ndarray
        Timepoints in seconds

    Returns
    -------
    np.ndarray
        Baseline corrected EEG, same shape
    """
    baseline_idx = times < 0
    baseline = eeg_data[:, :, baseline_idx].mean(axis=-1, keepdims=True)
    return eeg_data - baseline
