import React from 'react';
import { Card } from "antd";

const Post = ({post}) => {
    const { title, desc, author, created_at } = post;
    console.log(post);
    console.log(post.photos)
    return (
        <div>
            <Card hoverable>
                <Card.Meta/>
            </Card>
        </div>
    );
}

export default Post;