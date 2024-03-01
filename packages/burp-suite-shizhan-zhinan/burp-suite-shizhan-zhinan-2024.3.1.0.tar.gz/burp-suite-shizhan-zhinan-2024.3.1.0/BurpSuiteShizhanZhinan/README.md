# Burp Suite 实战指南

## 下载

### Docker

```
docker pull apachecn0/burp-suite-shizhan-zhinan
docker run -tid -p <port>:80 apachecn0/burp-suite-shizhan-zhinan
# 访问 http://localhost:{port} 查看文档
```

### PYPI

```
pip install burp-suite-shizhan-zhinan
burp-suite-shizhan-zhinan <port>
# 访问 http://localhost:{port} 查看文档
```

### NPM

```
npm install -g burp-suite-shizhan-zhinan
burp-suite-shizhan-zhinan <port>
# 访问 http://localhost:{port} 查看文档
```