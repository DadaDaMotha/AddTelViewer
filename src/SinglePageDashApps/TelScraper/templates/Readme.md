# Template Explanation

The DashCustomClass looks for files with the same name as defined in the placeholders.

```python
...

index = f'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8"/>                  
                {metas}     # from Dash package
                {custom_metas}
                <title>{static_page_title}</title>
                {custom_css_before}
                {css}       # from Dash package
                {custom_css_after}
            </head>
            <body>
                {inject_before_entrypoint}
                {main_wrapper} # is a function that substitutes {{custom_dash_entry}}
                {inject_after_entrypoint}
                {custom_scripts_body}
            </body>
            <footer>
                {config}    # from Dash package
                {self.custom_scripts_footer_before}
                {scripts}    # from Dash package
                {custom_scripts_footer_after}
            </footer>
        </html>
        ''')

```