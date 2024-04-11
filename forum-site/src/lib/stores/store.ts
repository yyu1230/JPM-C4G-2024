import { writable } from 'svelte/store';
import type { ForumPost } from "$lib/bindings/ForumPost";
import type { ForumComment } from '$lib/bindings/ForumComment';


export const forumPosts = writable<ForumPost[]>([]);
export const forumComments = writable<ForumComment[]>([]);