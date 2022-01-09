import React, { useEffect, useState } from 'react'
import axios from 'axios';
import Post from './Post';

const API_URL = "http://127.0.0.1:8000/posts/postlist/"

const PostList = () => {
    const [postList, setPostList] = useState([]);

    useEffect(() => {
        axios.get(API_URL)
        .then(res => {
            console.log("response", res);
            const { data } = res
            setPostList(data);
        })
        .catch(error => {
            console.log(error.response);
        })
    }, []);

    return (
        <div>
            {postList.map((post) => {
                return <Post post={post} key={post.id}/>
            })}
        </div>
    );
}

export default PostList;