from py2neo import Graph

"""python
# 环境安装
pip install py2neo
"""

class UpdateDensData():
    ''' 操作 neo4j 图数据库 '''

    def __init__(self):
        self.graph = Graph('http://192.168.31.220:7474', username='neo4j', password='123')

    def create_node(self, node_label, node_name):
        """创建节点"""
        cql = "MERGE(n:%s {name:'%s'})" % (str(node_label), str(node_name))
        cql = "create(n:node_label{name: 'node_name'})"
        self.graph.run(cql)

    def delete_node(self, node_name):
        """删除节点"""
        cql = "MATCH (n{name:'%s'})-[r]-() DELETE r" % (str(node_name))
        self.graph.run(cql)

    def update_node(self, node_name, new_name):
        """更新节点"""
        cql = "MATCH (n:{name: '%s'}) SET n.name='%s'" % (str(node_name), str(new_name))
        self.graph.run(cql)

    def search_node(self, node_name):
        """查找节点"""
        cql = "MATCH (n{name:'%s'}) RETURN n.name AS node_name" % (str(node_name))
        self.graph.run(cql)


if __name__ == '__main__':
    udd = UpdateDensData()