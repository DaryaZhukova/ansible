class FilterModule(object):
    def filters(self):
        return {
            'getid': self.getid,
}
    def getid(self, mydicts, value='Identity'):
        for x in mydicts:
            if x['name'] == value:
                return x['id']
