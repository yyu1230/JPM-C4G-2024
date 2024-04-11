<script context="module" lang="ts">
    import type { ForumPost } from "$lib/bindings/ForumPost";
    import { forumPosts } from '$lib/stores/store';
    import { get } from 'svelte/store';
    export async function load({ params }) {
        const { id } = params;
        const posts: ForumPost[] = get(forumPosts);
        console.log(posts);
        console.log(id)
        const post = posts.find(post => post.id === id);

        if (!post) {
            return { status: 404, error: new Error('Post not found') };
        }

        return { props: { post } };
    }
</script>

<script lang="ts">
    export let post: ForumPost;
</script>

<h1>{post}</h1>
