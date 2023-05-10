![LangChain](https://repository-images.githubusercontent.com/638822415/4d2a0cb5-e353-4182-933c-7935468d8f55)
# Kinsta - Hello World - LangChain

An example of how to deploy a Flask application with [LangChain](https://python.langchain.com/en/latest/index.html) on Kinsta App Hosting services.

---
Kinsta is a developer-centric cloud host / PaaS. We’re striving to make it easier for you to share your web projects with your users. Focus on coding and building, and we’ll take care of deployment and provide fast, scalable hosting. + 24/7 expert-only support.

- [Start your free trial](https://kinsta.com/signup/?product_type=app-db)
- [Application Hosting](https://kinsta.com/application-hosting)
- [Database Hosting](https://kinsta.com/database-hosting)

## Dependency Management

During the deployment process Kinsta will automatically install dependencies defined in your `requirements.txt` file.

## Web Server Setup

### Build Environment

When deploying your LangChain app, make sure to choose Dockerfile method as your build environment.

### Environment Variables

<details>

<summary>ℹ️ OpenAI models</summary>

In this example, we chose OpenAI's models for the sake of simplicity, but you're free to choose the models you prefer as LangChain provides support for other models as well. In that case, we recommend you remove the `OPENAI_API_KEY` environment variable and the relevant application code.

</details>

To ensure your successful deployment, set the following environment variables:

```bash
# Get it from https://platform.openai.com/account/api-keys
OPENAI_API_KEY=<YOUR_API_KEY>
```

## What is LangChain
LangChain framework is intended to develop language model-powered applications that are data-aware, agentic, and differentiated. More information is available on the [LangChain](https://python.langchain.com/en/latest/index.html) website.