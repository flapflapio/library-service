#!/usr/bin/env python3

from library_service.dataaccess.sql.postgres_sql_store import PostgresStore


# Runs the app in development mode
def main() -> None:
    demo_db()
    # uvicorn.run("library_service.main:app", host="localhost", port=8080, reload=True)


def demo_db() -> None:
    """A demo of how to utilize the database"""
    pgstore = PostgresStore()
    pgstore.save_file("jeff1", "somefile1.txt")
    pgstore.save_files("jeff1", "somefile1.txt", "file2.text")
    f = pgstore.load_file("jeff", "somefile.txt")
    print(f)


if __name__ == "__main__":
    main()
