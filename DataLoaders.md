## FILE-BASED LOADERS

| Loader Name                      | Module Path                            | Data Source  | Best Use Case in RAG                  |
| -------------------------------- | -------------------------------------- | ------------ | ------------------------------------- |
| `TextLoader`                     | `langchain_community.document_loaders` | `.txt` files | Simple knowledge base from text files |
| `PyPDFLoader`                    | `langchain_community.document_loaders` | PDF files    | PDF document QA system                |
| `UnstructuredPDFLoader`          | `langchain_community.document_loaders` | PDF          | Better layout-aware PDF parsing       |
| `PDFMinerLoader`                 | `langchain_community.document_loaders` | PDF          | Extract raw text from complex PDFs    |
| `Docx2txtLoader`                 | `langchain_community.document_loaders` | `.docx`      | Word document knowledge ingestion     |
| `UnstructuredWordDocumentLoader` | `langchain_community.document_loaders` | `.doc/.docx` | Structured Word parsing               |
| `CSVLoader`                      | `langchain_community.document_loaders` | `.csv`       | Structured data Q&A                   |
| `UnstructuredCSVLoader`          | `langchain_community.document_loaders` | `.csv`       | More flexible CSV parsing             |
| `JSONLoader`                     | `langchain_community.document_loaders` | `.json`      | JSON-based RAG datasets               |
| `UnstructuredJSONLoader`         | `langchain_community.document_loaders` | `.json`      | Nested JSON ingestion                 |
| `BSHTMLLoader`                   | `langchain_community.document_loaders` | HTML         | Clean HTML extraction                 |
| `UnstructuredHTMLLoader`         | `langchain_community.document_loaders` | HTML         | Structured website ingestion          |
| `MarkdownLoader`                 | `langchain_community.document_loaders` | `.md`        | Documentation RAG                     |
| `NotebookLoader`                 | `langchain_community.document_loaders` | `.ipynb`     | Code notebook Q&A                     |
| `PythonLoader`                   | `langchain_community.document_loaders` | `.py`        | Codebase RAG                          |

## DIRECTORY & BULK LOADERS

| Loader Name          | Module Path                            | Data Source     | Best Use Case                     |
| -------------------- | -------------------------------------- | --------------- | --------------------------------- |
| `DirectoryLoader`    | `langchain_community.document_loaders` | Folder of files | Bulk ingestion for enterprise RAG |
| `RecursiveUrlLoader` | `langchain_community.document_loaders` | Website         | Crawl entire documentation site   |
| `SitemapLoader`      | `langchain_community.document_loaders` | Website Sitemap | Structured site ingestion         |

## WEB & API LOADERS

| Loader Name             | Module Path                            | Data Source       | Best Use Case            |
| ----------------------- | -------------------------------------- | ----------------- | ------------------------ |
| `WebBaseLoader`         | `langchain_community.document_loaders` | Web pages         | Single-page RAG          |
| `UnstructuredURLLoader` | `langchain_community.document_loaders` | URLs              | Flexible webpage parsing |
| `PlaywrightURLLoader`   | `langchain_community.document_loaders` | JS-heavy websites | Dynamic site scraping    |
| `WikipediaLoader`       | `langchain_community.document_loaders` | Wikipedia         | Research assistant RAG   |
| `ArxivLoader`           | `langchain_community.document_loaders` | arXiv papers      | Academic RAG             |
| `PubMedLoader`          | `langchain_community.document_loaders` | PubMed            | Medical research QA      |
| `RSSFeedLoader`         | `langchain_community.document_loaders` | RSS feeds         | News monitoring RAG      |

## DATABASE LOADERS

| Loader Name         | Module Path                            | Data Source      | Best Use Case            |
| ------------------- | -------------------------------------- | ---------------- | ------------------------ |
| `SQLDatabaseLoader` | `langchain_community.document_loaders` | SQL DB           | Enterprise DB RAG        |
| `DataFrameLoader`   | `langchain_community.document_loaders` | Pandas DataFrame | In-memory structured RAG |
| `MongoDBLoader`     | `langchain_community.document_loaders` | MongoDB          | NoSQL document retrieval |


## CLOUD STORAGE LOADERS

| Loader Name              | Module Path                            | Data Source  | Best Use Case                |
| ------------------------ | -------------------------------------- | ------------ | ---------------------------- |
| `S3FileLoader`           | `langchain_community.document_loaders` | AWS S3       | Cloud-based document RAG     |
| `AzureBlobStorageLoader` | `langchain_community.document_loaders` | Azure Blob   | Enterprise cloud RAG         |
| `GoogleDriveLoader`      | `langchain_community.document_loaders` | Google Drive | Personal/team knowledge base |


## PRODUCTIVITY AND COLLABORATION TOOLS

| Loader Name          | Module Path                            | Data Source | Best Use Case                 |
| -------------------- | -------------------------------------- | ----------- | ----------------------------- |
| `NotionLoader`       | `langchain_community.document_loaders` | Notion      | Personal knowledge assistant  |
| `ConfluenceLoader`   | `langchain_community.document_loaders` | Confluence  | Company documentation RAG     |
| `SlackLoader`        | `langchain_community.document_loaders` | Slack       | Conversation search assistant |
| `GitHubIssuesLoader` | `langchain_community.document_loaders` | GitHub      | Developer support bot         |
| `JiraLoader`         | `langchain_community.document_loaders` | Jira        | Project management QA         |


## MULTIMEIDIA LOADERS

| Loader Name           | Module Path                            | Data Source         | Best Use Case           |
| --------------------- | -------------------------------------- | ------------------- | ----------------------- |
| `YoutubeLoader`       | `langchain_community.document_loaders` | YouTube transcripts | Video-based RAG         |
| `OpenAIWhisperLoader` | `langchain_community.document_loaders` | Audio files         | Audio transcription RAG |
