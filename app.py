#!/usr/bin/env python3

import uvicorn


# Runs the app in development mode
def main() -> None:
    uvicorn.run("library_service.main:app", host="localhost", port=8080, reload=True)


if __name__ == "__main__":
    main()
