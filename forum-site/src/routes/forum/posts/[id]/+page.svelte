<script lang="ts">
    import type { ForumPost } from "$lib/bindings/ForumPost";
    import { onMount } from "svelte";
    export let data;
    let formPost = data.post
    console.log(data.comments)
</script>

<style>
    .title {
        text-align: center;
        background-color: #f0f0f0;
        padding-top: 10px;
    }
    .content {
        background-color: #e0e0e0;
        padding-left: 20px;
    }
</style>

<h1 class="title">{formPost.title}</h1>
<p class="content">{formPost.content}</p>
