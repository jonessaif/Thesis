# Training on our Hindi Dataset : HDRS
### Note: Added **DNN-encoder** in **models.py**. To train NBT-DNN change the **model_type** variable in **config/woz_stat_update.cfg**.@ line no -- 43.

1. Extract the HDRS corpus files into **/data/woz/** directory.

2. Edit the **config/woz_stat_update.cfg** to take a speicified word vectors, i.e. [fasttext_sg_vector.vec](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding/indicnlp.v1.hi.vec.gz) to use it for training the NBT-CNN model.

3. Run the training script:
```
$ sh train.sh
  OR
$ python code/nbt.py train config/woz_stat_update.cfg
```

3. Run the testing script:
```
$ sh test.sh
  OR
$ python code/nbt.py woz config/woz_stat_update.cfg
```
4. Required conda environment
```
$ conda activate tf_gpu37
$ conda list
# packages in environment at /home/naive/.conda/envs/tf_gpu37:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
_tflow_select             2.1.0                       gpu  
absl-py                   0.9.0                    py37_0  
asn1crypto                1.3.0                    py37_0  
astor                     0.8.0                    py37_0  
blas                      1.0                         mkl  
blinker                   1.4                      py37_0  
boto3                     1.12.18                  pypi_0    pypi
botocore                  1.15.18                  pypi_0    pypi
c-ares                    1.15.0            h7b6447c_1001  
ca-certificates           2020.6.24                     0  
cachetools                3.1.1                      py_0  
certifi                   2020.6.20                py37_0  
cffi                      1.14.0           py37h2e261b9_0  
chardet                   3.0.4                 py37_1003  
click                     7.0                      py37_0  
cloudpickle               1.3.0                    pypi_0    pypi
cryptography              2.8              py37h1ba5d50_0  
cudatoolkit               10.1.243             h6bb024c_0  
cudnn                     7.6.5                cuda10.1_0  
cupti                     10.1.168                      0  
cycler                    0.10.0                   pypi_0    pypi
detectron2                0.1.1+cu101              pypi_0    pypi
dill                      0.3.2                      py_0  
docutils                  0.15.2                   pypi_0    pypi
filelock                  3.0.12                   pypi_0    pypi
future                    0.18.2                   pypi_0    pypi
fvcore                    0.1.dev200308            pypi_0    pypi
gast                      0.2.2                    py37_0  
google-auth               1.11.2                     py_0  
google-auth-oauthlib      0.4.1                      py_2  
google-pasta              0.1.8                      py_0  
grpcio                    1.27.2           py37hf8bcb03_0  
h5py                      2.10.0           py37h7918eee_0  
hdf5                      1.10.4               hb1b8bf9_0  
idna                      2.8                      py37_0  
intel-openmp              2020.0                      166  
jmespath                  0.9.5                    pypi_0    pypi
joblib                    0.14.1                   pypi_0    pypi
keras                     2.3.1                         0  
keras-applications        1.0.8                      py_0  
keras-base                2.3.1                    py37_0  
keras-preprocessing       1.1.0                      py_1  
kiwisolver                1.1.0                    pypi_0    pypi
ld_impl_linux-64          2.33.1               h53a641e_7  
libedit                   3.1.20181209         hc058e9b_0  
libffi                    3.2.1                hd88cf55_4  
libgcc-ng                 9.1.0                hdf63c60_0  
libgfortran-ng            7.3.0                hdf63c60_0  
libprotobuf               3.11.4               hd408876_0  
libstdcxx-ng              9.1.0                hdf63c60_0  
markdown                  3.1.1                    py37_0  
matplotlib                3.2.0                    pypi_0    pypi
mkl                       2020.0                      166  
mkl-service               2.3.0            py37he904b0f_0  
mkl_fft                   1.0.15           py37ha843d7b_0  
mkl_random                1.1.0            py37hd6b4f25_0  
ncurses                   6.1                  he6710b0_1  
numpy                     1.18.1           py37h4f9e942_0  
numpy-base                1.18.1           py37hde5b4d6_1  
oauthlib                  3.1.0                      py_0  
openssl                   1.1.1g               h7b6447c_0  
opt_einsum                3.1.0                      py_0  
panda                     0.3.1                    pypi_0    pypi
pandas                    1.0.1            py37h0573a6f_0  
pillow                    7.0.0                    pypi_0    pypi
pip                       20.0.2                   py37_1  
portalocker               1.5.2                    pypi_0    pypi
protobuf                  3.11.4           py37he6710b0_0  
pyasn1                    0.4.8                      py_0  
pyasn1-modules            0.2.7                      py_0  
pycparser                 2.19                     py37_0  
pydot                     1.4.1                    pypi_0    pypi
pyjwt                     1.7.1                    py37_0  
pyopenssl                 19.1.0                   py37_0  
pyparsing                 2.4.6                    pypi_0    pypi
pysocks                   1.7.1                    py37_0  
python                    3.7.6                h0371630_2  
python-dateutil           2.8.1                      py_0  
pytz                      2019.3                     py_0  
pyyaml                    5.3              py37h7b6447c_0  
readline                  7.0                  h7b6447c_5  
regex                     2020.2.20                pypi_0    pypi
requests                  2.22.0                   py37_1  
requests-oauthlib         1.3.0                      py_0  
rsa                       4.0                        py_0  
s3transfer                0.3.3                    pypi_0    pypi
sacremoses                0.0.38                   pypi_0    pypi
scikit-learn              0.22.1                   pypi_0    pypi
scipy                     1.4.1            py37h0b6359f_0  
sentencepiece             0.1.85                   pypi_0    pypi
setuptools                45.2.0                   py37_0  
six                       1.14.0                   py37_0  
sklearn                   0.0                      pypi_0    pypi
sqlite                    3.31.1               h7b6447c_0  
tabulate                  0.8.6                    pypi_0    pypi
tensorboard               2.1.0                     py3_0  
tensorflow                2.1.0           gpu_py37h7a4bb67_0  
tensorflow-base           2.1.0           gpu_py37h6c5654b_0  
tensorflow-estimator      2.1.0              pyhd54b08b_0  
tensorflow-gpu            2.1.0                h0d30ee6_0  
termcolor                 1.1.0                    py37_1  
tk                        8.6.8                hbc83047_0  
tokenizers                0.5.2                    pypi_0    pypi
torch                     1.4.0                    pypi_0    pypi
tqdm                      4.43.0                   pypi_0    pypi
transformers              2.5.1                    pypi_0    pypi
urllib3                   1.25.8                   py37_0  
werkzeug                  1.0.0                      py_0  
wheel                     0.34.2                   py37_0  
wrapt                     1.11.2           py37h7b6447c_0  
xz                        5.2.4                h14c3975_4  
yacs                      0.1.6                    pypi_0    pypi
yaml                      0.1.7                had09818_2  
zlib                      1.2.11               h7b6447c_3
```
### Results obtained on 22 May:
```
REQ - slot price range 0.985 0.649 0.783
REQ - slot food 0.979 0.737 0.841
REQ - slot area 0.994 0.909 0.95
{
    "price range": 0.649,
    "food": 0.737,
    "area": 0.909,
    "joint": 0.581
}
```

# Neural Belief Tracker

Contact: Nikola Mrkšić (nikola.mrksic@gmail.com)

An implementation of the Fully Data-Driven version of the Neural Belief Tracking (NBT) model (ACL 2018, [Fully Statistical Neural Belief Tracking](https://arxiv.org/abs/1805.11350)).  

This version of the model uses a learned belief state update in place of the rule-based mechanism used in the original paper. Requests are not a focus of this paper and should be ignored in the output.  

### Configuring the Tool

The config file in the config directory specifies the model hyperparameters, training details, dataset, ontologies, etc.

### Running Experiments

train.sh and test.sh can be used to train and test the model (using the default config file).
track.sh uses the trained models to 'simulate' a conversation where the developer can enter sequential user turns and observe the change in belief state.
