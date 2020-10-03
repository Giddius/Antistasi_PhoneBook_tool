@rem taskarg: ${file}
@Echo off

call ..\.venv\Scripts\activate

call memory_profiling_time.cmd ..\src\__main__.py
