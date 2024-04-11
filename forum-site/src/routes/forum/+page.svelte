<script lang='ts'>
    import type { ForumPost } from "$lib/bindings/ForumPost";
    import ForumHead  from "$lib/components/ForumHead.svelte";
	import { fetchPosts } from "$lib/utils";
	import { get } from "svelte/store";

    let posts = fetchPosts();


</script>

{#await posts}
    <p>Loading...</p>
{:then posts}
    {#each posts as post}
        <ForumHead post={post} />
    {/each}
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}
