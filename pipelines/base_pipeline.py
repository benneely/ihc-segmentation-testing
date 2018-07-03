from .common_utils.utils import get_training_data_for_image_set, find_overlapping_regions
import abc


class Pipeline(object):
    def __init__(self, image_set_dir, test_img_index=0):
        # get labeled ground truth regions from given image set
        self.training_data = get_training_data_for_image_set(image_set_dir)
        self.test_img_name = sorted(self.training_data.keys())[test_img_index]
        self.test_results = None

    @abc.abstractmethod
    def train(self):
        pass

    @abc.abstractmethod
    def test(self):
        pass

    def report(self):
        return find_overlapping_regions(
            self.training_data[self.test_img_name],
            self.test_results
        )
