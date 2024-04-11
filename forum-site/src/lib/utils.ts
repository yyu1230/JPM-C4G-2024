import type { ForumPost } from "$lib/bindings/ForumPost";
export async function fetchPosts() {
    try {
        const response = await fetch("http://127.0.0.1:5000/posts", {
            method : 'GET'
        });
        const data = await response.json();
        console.log(data);

    }
    catch (error) {
        console.error(error);
    }
}