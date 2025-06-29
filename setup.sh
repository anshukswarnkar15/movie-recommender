mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"24f2000476@ds.study.iitm.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = \$PORT\n\
" > ~/.streamlit/config.toml
