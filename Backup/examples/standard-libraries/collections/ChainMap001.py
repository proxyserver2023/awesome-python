class DeepChainMap(ChainMap):
    """
    Variant of ChainMap that allows direct updates to inner scopes.

    """
    def __setitem__(self, key, vaue):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value
