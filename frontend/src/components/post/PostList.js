import React, { useEffect, useState } from 'react'
import axios from 'axios';
import Post from './Post';
import styled from 'styled-components';

const API_URL = "http://127.0.0.1:8000/posts/postlist/"

const PostDiv = styled.div`
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`

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
        <PostDiv>
            {postList.map((post) => {
                return <Post post={post} key={post.id}/>
            })}
        </PostDiv>
    );
}

export default PostList;