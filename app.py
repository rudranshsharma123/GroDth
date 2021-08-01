from flows.execute import MyIndexer
import os
from jina import Document
from jina.flow.base import Flow
# from jina.executors import BinaryPbIndexer
import csv
import click
import sys
from config import encoder, model, max_docs
from untils.utils import docs_gen, check_workspace

indexer = MyIndexer

port = 12345
workspace_dir = os.path.join(os.path.abspath('workspace'))
print(workspace_dir)
def index(num_docs = max_docs):
    f = (
        Flow()
        .add(
            uses=encoder,
            pretrained_model_name_or_path=model,
            name="encoder",
            max_length=50,
        )
        .add(uses=indexer, workspace=workspace_dir, name="indexer", dump_path=workspace_dir)
    )
    with f:
        f.post(on='/index', inputs=docs_gen(), request_size=64, read_mode ='r')

def query():
    flow = (
        Flow()
        .add(
            uses=encoder,
            pretrained_model_name_or_path=model,
            name="encoder",
            max_length=50,
        )
        .add(uses=indexer, workspace=workspace_dir, name="indexer", dump_path=workspace_dir)
    )

    with flow:
        flow.protocol = "http"
        flow.port_expose = port
        flow.block()


def test():
    o = MyIndexer()
    x = o.search()
    for i in x:
        # print(x['hash'])
        print(type(x))
        print(x)


# index()
@click.command()
@click.option(
    "--task",
    "-t",
    type=click.Choice(["index", "query", "test"], case_sensitive=False),
)
@click.option("--num_docs", "-n", default=max_docs)

def main(task, num_docs):
    if task == 'index':
        # check_workspace(dir_name= workspace_dir, should_exist= True)
        index(num_docs= num_docs)   

    if task == 'query':
        check_workspace( dir_name= workspace_dir, should_exist=True)
        query()
    if task == 'test':
        test()


if __name__ == '__main__':
    main()

