
<br>

<div align=center>
<h1 aligh="center">
<img src="docs/logo.png" width="40"> AEL: Algorithm Evolution using Large Language Model
</h1>
[![Github][Github-image]][Github-url]
[![License][License-image]][License-url]
[![Releases][Releases-image]][Releases-url]
[![Web Demo][Installation-image]][Web Demo-url]
[![Wiki][Wiki-image]][Wiki-url]


[Github-image]: https://img.shields.io/badge/github-12100E.svg?style=flat-square
[License-image]: https://img.shields.io/github/license/binary-husky/gpt_academic?label=License&style=flat-square&color=orange
[Releases-image]: https://img.shields.io/github/release/binary-husky/gpt_academic?label=Release&style=flat-square&color=blue
[Installation-image]: https://img.shields.io/badge/dynamic/json?color=blue&url=https://raw.githubusercontent.com/binary-husky/gpt_academic/master/version&query=$.version&label=Installation&style=flat-square
[Wiki-image]: https://img.shields.io/badge/wiki-参考文档-black?style=flat-square


[Github-url]: https://github.com/FeiLiu36/AEL
[License-url]: https://github.com/FeiLiu36/AEL/LICENSE
[Releases-url]: https://github.com/FeiLiu36/AEL/releases
[Web Demo-url]: https://github.com/FeiLiu36/AEL/ael/app/
[Wiki-url]: https://github.com/FeiLiu36/AEL/docs/



</div>
<br>
This code provides a framework for **Evolutionary Computation** + **Large Language Model** for automatic algorithm design.

<img src="./docs/figures/ael.jpg" alt="ael" width="600" height="280">

## Introduction



If you are interested on LLM&Opt or AEL, you can:

1) Join LLM4Opt in Slack, 
2) Join Wechat Group, 
3) Contact us through email.

If you encounter any difficulty using the code, you can contact use thought the above or submit an [issue] 



Our implementation of **FunSearch, Deepmind** as the baseline, can be found [here](./baseline)





## A Quick Web Demo

A Quick Web Demo can be found [here](./ael/ap)





## Examples using AEL

#### Step 1: Install AEL

```bash
cd ael

pip install .
```

#### Step 2: Try Example: Greedy Algorithm for TSP

```bash
cd ael/examples/greedy_tsp

python runAEL.py
```

### More Examples using AEL (Code & Paper)

#### Combinatorial Optimization

1. Online Bin Packing, greedy heuristic, [code](./ael/examples/online_bin_packing), [paper]
2. TSP, construct heuristic, [code](./ael/examples/greedy_tsp), [paper]
3. TSP, guided local search, [code], [paper]
4. Flow Shop Scheduling Problem (FSSP), guided local search, [code], [paper]

#### Machine Learning

1. Attack, , [code](./ael/examples/L_AutoDA), [paper](https://arxiv.org/abs/2401.15335)

#### Bayesian Optimization

1. 



## Use AEL in You Application

A Step-by-step guide is provided in [here](./docs/guide/AEL_Usage.md)



## Files in ael

+ **ael.py**: main ael
+ **ec**:
  + interface_EC.py: interface for ec
  + evolution.py: evolution operators
  + management.py: population management
  + selection.py: parents selection
+ **llm**
  + interface_LLM.py: interface for LLM
  + api_api2d.py: api2d api for GPT
  + others
+ utils:
  + some util functions

**Current support:**

+ **ECs:** 
  + 1i: design a new algorithm without any in-context inf.
  + e1: design an algorithm totally different from existing ones
  + e2: identify the common patterns in existing algorithms, design a new algorithm
  + m1: design a new algorithm modified from existing one
  + m2: do not design new algorithm, try different parameter settings
+ **LLMs:** 
  + API2D (https://api2d.com/) or OpenAI interface for GPT3.5 and GPT4. (Paid)
  + Huggingface interface (Free), in testing
  + Local model Llama2, in testing
  + If you want to use other LLM or if you want to use your own GPT API or local LLMs, please add your interface in ael/llm
+ population management:
  + delete worst
+ selection:
  + probability
  + 





## Reference Papers

1. **AEL**:  "Fei Liu, Xialiang Tong, Mingxuan Yuan, and Qingfu Zhang, Algorithm Evolution Using Large Language Model. arXiv preprint arXiv:2311.15249. 2023."  https://arxiv.org/abs/2311.15249
2. **Guided Local Search:** "Fei Liu, Xialiang Tong, Mingxuan Yuan, Xi Lin, Fu Luo, Zhenkun Wang, Zhichao Lu, and Qingfu Zhang, [An Example of Evolutionary Computation+ Large Language Model Beating Human: Design of Efficient Guided Local Search](https://arxiv.org/abs/2401.02051)" https://arxiv.org/abs/2401.02051
3. **Adversarial Attacks:** Pin Guo, Fei Liu, Xi Lin, Qingchuan Zhao, and Qingfu Zhang,  L-AutoDA: Leveraging Large Language Models for Automated Decision-based Adversarial Attacks. *arXiv preprint arXiv:2401.15335*. 2024.



## License

MIT
