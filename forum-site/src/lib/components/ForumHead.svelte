<script lang='ts'>
    import type { ForumPost } from "$lib/bindings/ForumPost";

    export let post : ForumPost;
</script>


<style>
    .forum-head {
        display: flex;
        justify-content: space-between;
        width: 100%;
        height: 50px;
        border: 1px solid #ccc;
        padding: 10px;
        margin-bottom: 10px;
    }

    .title {
        font-weight: bold;
    }

    .preview {
        color: #666;
    }

    .info {
        text-align: right;
    }
</style>

<div class="forum-head">
    <div>
        <div class="title">{post.title}</div>
        <div class="preview">{post.content.substring(0, 50)}...</div>
    </div>
    <div class="info">
        <div>{post.author}</div>
        <div>{post.created}</div>
    </div>
</div>