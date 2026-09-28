import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Enviroweather API Documentation (v1)


    1. [Getting Started](ewx_api_v1_intro.html)
    2. ...more come
    """)
    return


if __name__ == "__main__":
    app.run()
