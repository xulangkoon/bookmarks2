/*我们的Javascript保存在后端，用户通过url来获取这段Javascript，
而url有这段Javascript来随机生成，
这就是一个书签激活脚本。
这样做的好处是当我们更新了我们后端的js文件后，不需要用户更新书签就能够更新我们的代码
*/

(function(){
    if(window.myBookmarklet!==undefined){
        myBookmarklet();
    }
    // 如果myBookmarklet还没有被加载在文档中添加一个<script>元素，source是来自与bookmarklet.js,我们可以随时更新这个bookmarklet.js而不用用户更新书签。
    else{
        document.body.appendChild(document.createElement('script')).src='http://127.0.0.1:8000/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();