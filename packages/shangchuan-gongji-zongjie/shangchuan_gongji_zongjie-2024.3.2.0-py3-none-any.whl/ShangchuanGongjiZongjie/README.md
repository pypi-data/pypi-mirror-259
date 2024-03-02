# 上传攻击总结

## 下载

### Docker

```
docker pull apachecn0/shangchuan-gongji-zongjie
docker run -tid -p <port>:80 apachecn0/shangchuan-gongji-zongjie
# 访问 http://localhost:{port} 查看文档
```

### PYPI

```
pip install shangchuan-gongji-zongjie
shangchuan-gongji-zongjie <port>
# 访问 http://localhost:{port} 查看文档
```

### NPM

```
npm install -g shangchuan-gongji-zongjie
shangchuan-gongji-zongjie <port>
# 访问 http://localhost:{port} 查看文档
```