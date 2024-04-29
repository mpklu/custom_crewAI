# An example of using custom crew AI

This is a modified version of CrewAI's [azure-model](https://github.com/joaomdmoura/crewAI-examples/tree/main/azure_model) example.

We use it here simply to demonstrate how to use CrewAI from local source code.

## Steps to import crewAI from source code

### 1. Clone crew AI from GitHub

This custom Crew AI fork:

```
git clone https://github.com/mpklu/custom_crewAI.git
```

or the original Crew AI

```
git clone https://github.com/joaomdmoura/crewai.git

```

### 2. Setting Up Dependencies

Add crewAI's dependenies to your App's `requirements.txt`

```
    agentops==0.1.6
    appdirs==1.4.4
    click==8.1.7
    crewai-tools==0.1.7
    embedchain==0.1.98
    instructor==0.5.2
    langchain
    langchain-community
    langchain-core
    langchain-openai
    openai
    opentelemetry-api==1.22.0
    opentelemetry-exporter-otlp-proto-http==1.22.0
    opentelemetry-sdk==1.22.0
    pydantic==2.7.0
    python-dotenv==1.0.0
    regex
```

Above are the common libraries you need to run Crew AI, you might adjust to fit your need.

Then install the dependencies

```
    pip install -r requirements.txt
```

### 3. Adding CrewAI to Your Python Path

```
    crewai_path = os.getenv("LOCAL_CREWAI_PATH")
    sys.path.append(crewai_path)
```

\

### 4. Using CrewAI Modules

Once you've set up the source code and its dependencies, you can directly import and use CrewAI's modules in your scripts:

```
    from crewai import Agent, Task, Crew, Process
```
