
# streamlit-analytics2 &nbsp;👀

[![PyPi](https://img.shields.io/pypi/v/streamlit-analytics2)](https://pypi.org/project/streamlit-analytics2/)

**Enhanced tracking & visualization for your Streamlit apps.**

`streamlit-analytics2` is a fork and extension of the original [streamlit-analytics](https://github.com/jrieke/streamlit-analytics), aimed at improving and securing the analytics functionality within Streamlit applications. With minimal setup, track user interactions and visualize analytics directly in your browser, akin to Google Analytics but tailored for Streamlit.

This fork was initiated due to the inability to collaborate directly on the upstream project, which currently has several unresolved security issues and bugs. Our intention is to maintain a positive relationship with the original project and its creator, focusing on enhancing the tool's reliability and security for the community.

<sup>This project is in active development. We welcome contributions and address security concerns on a best-effort basis, with details available in our [SECURITY.md](.github/SECURITY.md).</sup>

---

<h3 align="center">
  🎈 <a href="https://share.streamlit.io/jrieke/streamlit-analytics2/main/examples/pages/sharing-demo.py?analytics=on">Live Demo</a> 🎈
</h3>

---

<p align="center">
    <a href="https://share.streamlit.io/jrieke/streamlit-analytics2/main/examples/sharing-demo.py?analytics=on"><img src="images/example.png" width=600></a>
</p>

## Installation

```bash
pip install streamlit-analytics2
```

## How to Use

Simple integration with any Streamlit app:

```python
import streamlit as st
import streamlit_analytics2 as streamlit_analytics

with streamlit_analytics.track():
    st.text_input("Write something")
    st.button("Click me")
```
> [!IMPORTANT]
> The alias ```import streamlit_analytics2 as streamlit_analytics``` allows for backwards compatibility and reduces any unecessary changes in your exisitng codebase. Check out our [Migration Guide](https://github.com/444B/streamlit-analytics2/wiki/0.--Migration-Guide-from-streamlit%E2%80%90analytics-to-streamlit%E2%80%90analytics2) for more info.

All interactions are now tracked, supporting all standard Streamlit widgets.

## Moving Forward

- **TODOs and Feature Requests**: We've transitioned our roadmap and feature requests to [GitHub Issues](https://github.com/your-repo/streamlit-analytics2/issues). Feel free to contribute ideas or report bugs!
- **Advanced Configuration**: Detailed guidance on advanced setup (inlcuding password protection and database integration) options is available in our [Project Wiki](https://github.com/444B/streamlit-analytics2/wiki).

## Contributing

Your contributions are welcome! Please refer to our [CONTRIBUTING.md](.github/CONTRIBUTING.md) for guidelines on how to make a difference.

## Security

We prioritize the security of our users' data. For reporting security vulnerabilities or for more information, please review our [SECURITY.md](.github/SECURITY.md).

## Acknowledgments

A special thanks to [jrieke](https://github.com/jrieke) and all contributors to the original `streamlit-analytics` project. Your work has inspired continued innovation and community collaboration.
