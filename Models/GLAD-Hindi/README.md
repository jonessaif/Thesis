# Training on our Hindi Dataset : HDRS
1. Extract the HDRS corpus files into **/data/woz_hin/raw** directory.
2. Run **preprocess_data.py** script with required embedding file name @ line no-67
```
emb_file = "../EMBEDDINGS/fasttext_sg.json"
```
3. Run Training:
```
$ conda activate torch_gpu36
$ python train.py --gpu 0
```
4. Run Testing:
```
python evaluate.py --split test_hin exp/glad/default
```
5. Required conda environment
```
$ conda activate torch_gpu36
$ conda list
# packages in environment at /home/naive/.conda/envs/torch_gpu36:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
asn1crypto                1.3.0                    py36_0  
attrs                     19.3.0                   pypi_0    pypi
backcall                  0.1.0                    pypi_0    pypi
beautifulsoup4            4.9.1                    pypi_0    pypi
blas                      1.0                         mkl  
blis                      0.4.1                    pypi_0    pypi
boto                      2.49.0                   py36_0  
boto3                     1.12.47                  pypi_0    pypi
botocore                  1.15.47                  pypi_0    pypi
bottleneck                1.3.2                    pypi_0    pypi
bpemb                     0.3.0                    pypi_0    pypi
ca-certificates           2020.6.24                     0    anaconda
cachetools                3.1.1                      py_0  
catalogue                 1.0.0                    pypi_0    pypi
certifi                   2020.6.20                py36_0    anaconda
cffi                      1.14.0           py36h2e261b9_0  
chardet                   3.0.4                 py36_1003  
click                     7.1.2                    pypi_0    pypi
cloudpickle               1.5.0                    pypi_0    pypi
cmake                     3.17.3                   pypi_0    pypi
cryptography              2.8              py36h1ba5d50_0  
cycler                    0.10.0                   pypi_0    pypi
cymem                     2.0.3                    pypi_0    pypi
dataclasses               0.7                      pypi_0    pypi
decorator                 4.4.2                    pypi_0    pypi
deprecated                1.2.10                   pypi_0    pypi
dill                      0.3.2                      py_0  
docutils                  0.15.2                   pypi_0    pypi
embeddings                0.0.8                    pypi_0    pypi
fastai                    1.0.57                   pypi_0    pypi
fastprogress              0.2.3                    pypi_0    pypi
filelock                  3.0.12                   pypi_0    pypi
flair                     0.5.1                    pypi_0    pypi
future                    0.18.2                   pypi_0    pypi
gensim                    3.8.0            py36h962f231_0  
google-api-core           1.17.0                   py36_0  
google-auth               1.14.1                     py_0  
google-cloud-core         1.3.0                      py_0  
google-cloud-storage      1.28.0                     py_0  
google-resumable-media    0.5.0                      py_1  
googleapis-common-protos  1.51.0                   py36_2  
hyperopt                  0.2.4                    pypi_0    pypi
idna                      2.9                        py_1  
importlib-metadata        1.7.0                    pypi_0    pypi
intel-openmp              2020.1                      217  
ipdb                      0.13.2                   pypi_0    pypi
ipython                   7.13.0                   pypi_0    pypi
ipython-genutils          0.2.0                    pypi_0    pypi
jedi                      0.16.0                   pypi_0    pypi
jmespath                  0.9.5                    pypi_0    pypi
joblib                    0.16.0                   pypi_0    pypi
kiwisolver                1.2.0                    pypi_0    pypi
langdetect                1.0.8                    pypi_0    pypi
ld_impl_linux-64          2.33.1               h53a641e_7  
libedit                   3.1.20181209         hc058e9b_0  
libffi                    3.2.1                hd88cf55_4  
libgcc                    5.2.0                         0    conda-forge
libgcc-ng                 9.1.0                hdf63c60_0  
libgfortran-ng            7.3.0                hdf63c60_0  
libprotobuf               3.11.4               hd408876_0  
libstdcxx-ng              9.1.0                hdf63c60_0    anaconda
matplotlib                3.2.2                    pypi_0    pypi
mkl                       2020.1                      217  
mkl-service               2.3.0            py36he904b0f_0  
mkl_fft                   1.0.15           py36ha843d7b_0  
mkl_random                1.1.0            py36hd6b4f25_0  
more-itertools            8.4.0                    pypi_0    pypi
mpld3                     0.3                      pypi_0    pypi
murmurhash                1.0.2                    pypi_0    pypi
ncurses                   6.2                  he6710b0_0  
networkx                  2.4                      pypi_0    pypi
numexpr                   2.7.1                    pypi_0    pypi
numpy                     1.18.2                   pypi_0    pypi
numpy-base                1.18.1           py36hde5b4d6_1  
nvidia-ml-py3             7.352.0                  pypi_0    pypi
openssl                   1.1.1g               h7b6447c_0    anaconda
packaging                 20.4                     pypi_0    pypi
pandas                    1.0.5            py36h0573a6f_0  
parso                     0.6.2                    pypi_0    pypi
pexpect                   4.8.0                    pypi_0    pypi
pickleshare               0.7.5                    pypi_0    pypi
pillow                    7.2.0                    pypi_0    pypi
pip                       20.0.2                   py36_1  
plac                      1.1.3                    pypi_0    pypi
pluggy                    0.13.1                   pypi_0    pypi
preshed                   3.0.2                    pypi_0    pypi
prompt-toolkit            3.0.5                    pypi_0    pypi
protobuf                  3.11.3                   pypi_0    pypi
ptyprocess                0.6.0                    pypi_0    pypi
py                        1.9.0                    pypi_0    pypi
pyasn1                    0.4.8                      py_0  
pyasn1-modules            0.2.7                      py_0  
pycparser                 2.20                       py_0  
pygments                  2.6.1                    pypi_0    pypi
pyopenssl                 19.1.0                   py36_0  
pyparsing                 2.4.7                    pypi_0    pypi
pysocks                   1.7.1                    py36_0  
pytest                    5.4.3                    pypi_0    pypi
python                    3.6.10               hcf32534_1  
python-dateutil           2.8.1                      py_0  
pytorch-pretrained-bert   0.6.1                    pypi_0    pypi
pytorch-transformers      1.2.0                    pypi_0    pypi
pytz                      2020.1                     py_0  
pyyaml                    5.3.1                    pypi_0    pypi
readline                  8.0                  h7b6447c_0  
regex                     2020.4.4                 pypi_0    pypi
requests                  2.23.0                   py36_0  
rsa                       4.0                        py_0  
s3transfer                0.3.3                    pypi_0    pypi
sacremoses                0.0.43                   pypi_0    pypi
scikit-learn              0.23.1                   pypi_0    pypi
scipy                     1.4.1            py36h0b6359f_0  
segtok                    1.5.10                   pypi_0    pypi
sentencepiece             0.1.91                   pypi_0    pypi
setuptools                46.1.3                   py36_0  
six                       1.14.0                   py36_0  
smart_open                2.0.0                      py_0  
soupsieve                 2.0.1                    pypi_0    pypi
spacy                     2.3.0                    pypi_0    pypi
sqlite                    3.31.1               h7b6447c_0  
sqlitedict                1.6.0                    pypi_0    pypi
srsly                     1.0.2                    pypi_0    pypi
stanfordnlp               0.2.0                    pypi_0    pypi
stanza                    1.0.0                    pypi_0    pypi
tabulate                  0.8.7                    pypi_0    pypi
tensorboardx              1.6                      pypi_0    pypi
thinc                     7.4.1                    pypi_0    pypi
threadpoolctl             2.1.0                    pypi_0    pypi
tk                        8.6.8                hbc83047_0  
tokenizers                0.8.1rc2                 pypi_0    pypi
torch                     1.2.0                    pypi_0    pypi
torchtext                 0.3.1                    pypi_0    pypi
torchvision               0.6.1                    pypi_0    pypi
tqdm                      4.44.1                     py_0  
traitlets                 4.3.3                    pypi_0    pypi
transformers              3.1.0                    pypi_0    pypi
typing                    3.7.4.1                  pypi_0    pypi
urllib3                   1.25.8                   py36_0  
vocab                     0.0.4                    pypi_0    pypi
wasabi                    0.7.0                    pypi_0    pypi
wcwidth                   0.1.9                    pypi_0    pypi
wheel                     0.34.2                   py36_0  
wrapt                     1.12.1                   pypi_0    pypi
xz                        5.2.4                h14c3975_4  
zipp                      3.1.0                    pypi_0    pypi
zlib                      1.2.11               h7b6447c_3  

```
# Global-Locally Self-Attentive Dialogue State Tracker

This repository contains an implementation of the [Global-Locally Self-Attentive Dialogue State Tracker (GLAD)](https://arxiv.org/abs/1805.09655).
If you use this in your work, please cite the following

```
@inproceedings{ zhong2018global,
  title={ Global-Locally Self-Attentive Encoder for Dialogue State Tracking },
  author={ Zhong, Victor and Xiong, Caiming and Socher, Richard },
  booktitle={ ACL },
  year={ 2018 }
}
```


# Install dependencies

Using Docker

```
docker build -t glad:0.4 .
docker run --name embeddings -d vzhong/embeddings:0.0.5  # get the embeddings
env NV_GPU=0 nvidia-docker run --name glad -d -t --net host --volumes-from embeddings glad:0.4
```

If you do not want to build the Docker image, then run the following (you still need to have the CoreNLP server).

```
pip install -r requirements.txt
```

# Download and annotate data

This project uses Stanford CoreNLP to annotate the dataset.
In particular, we use the [Stanford NLP Stanza python interface](https://github.com/stanfordnlp/stanza).
To run the server, do

```
docker run --name corenlp -d -p 9000:9000 vzhong/corenlp-server
```

The first time you preprocess the data, we will [download word embeddings and character embeddings and put them into a SQLite database](https://github.com/vzhong/embeddings), which will be slow.
Subsequent runs will be much faster.

```
docker exec glad python preprocess_data.py
```

The raw data will be stored in `data/woz/raw` of the container.
The annotation results will be stored in `data/woz/ann` of the container.

If you do not want to build the Docker image, then run

```
python preprocess_data.py
```


# Train model

You can checkout the training options via `python train.py -h`.
By default, `train.py` will save checkpoints to `exp/glad/default`.

```
docker exec glad python train.py --gpu 0
```

You can attach to the container via `docker exec glad -it bin/bash` to look at what's inside or `docker cp glad /opt/glad/exp exp` to copy out the experiment results.

If you do not want to build the Docker image, then run

```
python train.py --gpu 0
```


# Evaluation

You can evaluate the model using

```
docker exec glad python evaluate.py --gpu 0 --split test exp/glad/default
```

You can also dump a predictions file by specifying the `--fout` flag.
In this case, the output will be a list of lists.
Each `i`th sublist is the set of predicted slot-value pairs for the `i`th turn.
Please see `evaluate.py` to see how to match up the turn predictions with the dialogues.

If you do not want to build the Docker image, then run

```
python evaluate.py --gpu 0 --split test exp/glad/default
```


# Contribution

Pull requests are welcome!
If you have any questions, please create an issue or contact the corresponding author at `victor <at> victorzhong <dot> com`.
