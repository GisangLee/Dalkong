import React from 'react';
import { Card } from "antd";
import styled from 'styled-components';

const BASE_URL = "http://localhost:8000"

const PostItem = styled.div`
    margin-bottom: 3rem;
`


const Post = ({post}) => {
    const { title, desc, author, created_at, photo } = post;
    console.log(post);
    console.log(photo[0].file);
    return (
        <PostItem>
            <Card
                hoverable
                style={{width:"100"}}
                cover={<img src={`${BASE_URL}${photo[0].file}`} alt={desc} width={"300px"} />}
            >
                <Card.Meta title={title} description={desc}/>
            </Card>
        </PostItem>
    );
}

export default Post;