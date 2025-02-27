class FeatureRegistry:
    def __init__(self):
        self.features = {}

    def register(self, name, description):
        self.features[name] = {
            'description': description,
            'is_active': True
        }

    def get_features(self):
        return self.features

feature_registry = FeatureRegistry()
