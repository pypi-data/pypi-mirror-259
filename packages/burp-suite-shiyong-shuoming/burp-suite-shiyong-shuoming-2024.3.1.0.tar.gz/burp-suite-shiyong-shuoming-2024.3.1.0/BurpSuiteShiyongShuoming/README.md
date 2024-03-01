# Burp Suite 使用说明

## 下载

### Docker

```
docker pull apachecn0/burp-suite-shiyong-shuoming
docker run -tid -p <port>:80 apachecn0/burp-suite-shiyong-shuoming
# 访问 http://localhost:{port} 查看文档
```

### PYPI

```
pip install burp-suite-shiyong-shuoming
burp-suite-shiyong-shuoming <port>
# 访问 http://localhost:{port} 查看文档
```

### NPM

```
npm install -g burp-suite-shiyong-shuoming
burp-suite-shiyong-shuoming <port>
# 访问 http://localhost:{port} 查看文档
```