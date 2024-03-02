<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="./images/brand.png">
  <img alt="Pandas Logo" src="./images/brand.png">
</picture>

# crypto-ai-agent: copilot your Web3 journey

[![license](https://img.shields.io/github/license/voltfin-crypto/crypto-ai-agent)](#license)
[![Python Version](https://img.shields.io/pypi/pyversions/crypto-ai-agent?style=flat)](https://pypi.org/project/crypto-ai-agent/)
[![PyPi Version](https://img.shields.io/pypi/v/crypto-ai-agent?style=flat)](https://pypi.org/project/crypto-ai-agent/)
[![Package Status](https://img.shields.io/pypi/status/crypto-ai-agent?style=flat)](https://pypi.org/project/crypto-ai-agent/)
[![Downloads](https://img.shields.io/pypi/dm/crypto-ai-agent?style=flat)](https://pypistats.org/packages/crypto-ai-agent)
[![Stars](https://img.shields.io/github/stars/voltfin-crypto/crypto-ai-agent?style=flat)](#stars)
[![Forks](https://img.shields.io/github/forks/voltfin-crypto/crypto-ai-agent?style=flat)](#forks)
[![Used By](https://img.shields.io/badge/used_by-170-orange.svg?style=flat)](#usedby)
[![Contributors](https://img.shields.io/github/contributors/voltfin-crypto/crypto-ai-agent?style=flat)](#contributors)
[![Issues](https://img.shields.io/github/issues-raw/voltfin-crypto/crypto-ai-agent?style=flat)](#issues)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/voltfin-crypto/crypto-ai-agent?style=flat)](#closed-issues)

## What is it?

**crypto-ai-agent** is your AI copilot during the exciting Web3 journey. It goes beyond the solely AGI trained by LLM which provides mainly chats. Using this package, users will take the power of AI and connects all the dots together, it is going to help you do the tedious work, 

 python package to help users create agents serve for different kinds of tasks in the Web3 and Crypto world. Crypto is fast-evolving with new knowledge everyday, keep learning and keep alerting is usually hard as there are so many opportunities to miss out. So, the best solution is, AI Agent! You can use this library to create your own AI Agents which feeds with different domain knowledge to do the tasks you assign to. This project is fully open source and you can use it as much as you want.

Training the agents is hard, and we do the hard part for you. This project is more like a wrap up toolbox for the immediate use of the power of AI. What you need to do is take the agents and formulate a team, which works best for you.

## Table of Contents

- [Main Features](#main-features)
- [Structure](#structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Help](#help)

## Main Features
Image that one day, when you wake up, you found that you are doing a space travel alone, you have no idea what it is, where it is, the only accompany is an AI agent called **crypto-ai-agent**, what do you expect it provides? That is the main features for this package, it will help the beginners learn the basic rules and experts shine in the space. 

So, high level speaking, there are 4 things we need to do to make sure our space travel successful: 
### 1. Learn the Rules
There are tons of rules created by different parties, but there are consensus, evolving, but exists. But we don't have time to learn it from primary school as it is a space travel, however, luckily we can learning from the reality. By using this package, you can:
- Use the framework to train the agent, which will provides Web3 explaination 
- Ask questions, take courses, take exams, take quiz, all the things will help you understand and grasp the knowledge of Web3 is provided
### 2. Collect Information
Information is the key, especially in this fast-pace world. It is hard to do it manually for all the chains, coins, protocols, but with the AI agents, it can highly abstrat this process and do it for you. 
- Collect coins price data
- Collect news information 
- Collect on-chain data
- Trace the addresses
- Collect the social media reaction 
### 3. Analyze Information 
Once we got the information, we need to take time to analyze it. 
- Analyze the prices trends
- Analyze the news
- Analyze the external off-chain metrics data and bring it on-chain for more advanced analtyics 
### 4. Take Actions
- Write the analytics reports
- Send alerts for unusal activities
- Streamline the data engineering process

## Structure
For the package, we got 2 main parts: **Model** and **Blueprint**, each model serve for 1 or more rules listed above. You ask why we strcuture the project like this, this is a little bit non-technical, shouldn't we do ` import abcd as ad` or `import func_abc from dsd`? Well, we can do that, that is also an option to use this package, but we don't recommend, as remember, this is a space travel, what you need to do is use it as fast as possible, and then when you got time, you can start learning the basic of the spaceship. 

### Model
- Professor (TODO)
- Analyst
- Engineer (TODO)
- Blacksmith (TODO)

### Blueprint (TODO)
In some cases, we need not only one type of role to do the jobs, but many roles should work togethere as a team per the instruction in Blueprint. To further support the automated work, we introduct Blueprint, which serves as a higher level of automated work, it is predesigned part of work and you don't need to create it

## Installation

The source code is currently hosted on GitHub at:
https://github.com/voltfin-crypto/crypto-ai-agent

```sh
# conda
conda install -c conda-forge crypto-ai-agent
```

```sh
# or PyPI
pip install crypto-ai-agent
```

## Quick Start
### Step 1: Configure your .env file locally
In the root directory, configure your `.env` file, make it something like:
```
COINGECKO_API_KEY="YOUR API KEY"
OPENAI_API_KEY="YOUR API KEY"
```
### Step 2: Use cases
#### Write Technical Analytics blogs
```python
from cagent import Analyst
analyst = Analyst("analyst")
analyst.run_technical_analytics("bitcoin", ["macd", "rsi"])
```

## Help

<hr>

[Go to Top](#table-of-contents)
