# Template Explanation

This is the folder to store your main wrapper template or you set another one in `settings.py` with
`REACT_WRAPPER`. This is the the entrypoint wrapped in a custom div:

```python

<div id="custom-div">
    <div id="react-entry-point">
        <div class="_dash-loading">
            Custom Loading...
        </div>
    </div>
</div>

```