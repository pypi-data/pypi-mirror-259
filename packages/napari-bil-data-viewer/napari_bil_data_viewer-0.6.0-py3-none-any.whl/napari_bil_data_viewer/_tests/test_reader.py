from napari_bil_data_viewer import napari_experimental_provide_dock_widget
from napari_bil_data_viewer.dataset_info import get_datasets

# Test that datasets return a dict
assert isinstance(get_datasets(), dict)


# Test whether dock widget is accessable
def test_provide_dock_widget():
    assert [callable(x) for x in napari_experimental_provide_dock_widget()]
