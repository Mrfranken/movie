# movie
#### 07.30
- 构建项目的目录结构（创建各种文件夹）

- 蓝图构建项目目录
    - 蓝图的功能
        - 蓝图将不同的功能模块化
        - 构建大型应用
        - 优化项目结构
        - 增强可读性，易于维护
    - 将蓝图放在不用目录中（home和admin）
    
- 会员、会员登录日志模型设计
- 电影、上映预告模型设计
- 电影评论、收藏模型设计
- 权限、角色模型设计

#### 07.31
- 首页页面搭建
- 登录、注册、退出页面（路由注册）

- 会用中心页面搭建
    - 会员中心
    - 修改密码
    - 评论记录
    - 登录日志
    - 收藏电影
    ```
    拆分 user.html change_password.html comments.html loginlog.html moviecol.html，将共同的部分拆分到user_base.html，
    并在 user_base.html 中添加 js 代码（根据url去添加active属性）
    ```

 