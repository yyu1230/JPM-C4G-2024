import type { ForumPost } from "$lib/bindings/ForumPost";
import type { ForumComment } from "$lib/bindings/ForumComment";
export async function fetchPosts() {
    try {
        const response = await fetch("http://127.0.0.1:5000/posts", {
            method : 'GET'
        });
        const data = await response.json();
        return data.map(item => {
            return {
                title: item.title,
                content: item.body,
                id: item.id,
                author: item.author,
                created: new Date().toISOString(), // replace with actual creation date if available
            } as ForumPost;
        });
        
    }
    catch (error) {
        console.error(error);
    }
}

export async function fetchComments(id) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/comments/${id}`, {
            method : 'GET'
        });
        const data = await response.json();
        return data.map(item => {
            return {
                id: item.postID,
                content: item.commentbody,
                author: item.author,
                created: new Date().toISOString(), // replace with actual creation date if available
            } as ForumComment;
        });

    }
    catch (error) {
        console.error(error);
    }
}

export async function postComment(id, comment) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/new_comment`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                postID: id,
                commentBody: comment,
                author: "You"
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error(error);
    }
}

export async function postPost(post : ForumPost) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/new_post`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: post.title,
                body: post.content,
                author: post.author,
                id: post.id
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data)
    } catch (error) {
        console.error(error);
    }
}

export async function chat(message: string) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data.message;
    } catch (error) {
        console.error(error);
    }
}