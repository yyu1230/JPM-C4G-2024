<script lang="ts">
    import type { ForumPost } from "$lib/bindings/ForumPost";
    import { onMount } from "svelte";
    export let post: ForumPost;
    export let data: ForumPost;



    onMount(() => {
        console.log("data below")
		console.log(data)
	});

    
</script>

<h1>{post}</h1>
<h1>{data}</h1>
