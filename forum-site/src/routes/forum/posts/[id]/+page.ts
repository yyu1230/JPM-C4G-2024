import type { ForumPost } from "$lib/bindings/ForumPost";
import { forumPosts } from '$lib/stores/store';
import { fetchPosts } from "$lib/utils.js";
import { get } from 'svelte/store';
export async function load({ params }) {
    const { id } = params;
    const posts: ForumPost[] = await fetchPosts();
    const post = posts.find(post => post.id === id);

    if (!post) {
        return { status: 404, error: new Error('Post not found') };
    }

    return { post };
}