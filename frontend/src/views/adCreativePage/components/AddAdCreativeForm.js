import {Button, Form, Input} from 'antd';
import React from 'react';
import {createAd, createAdCreative} from "../../../services/services";


const layout = {
    labelCol: {
        span: 8,
    },
    wrapperCol: {
        span: 16,
    },
};
const tailLayout = {
    wrapperCol: {
        offset: 8,
        span: 16,
    },
};

const AddAdCreativeForm = (props) => {
    const formRef = React.useRef(null);

    const onFinish = (values) => {
        props.setVisible(false);
        let data = {
            name: values.name,
            object_story_spec: {
                page_id: values.page_id,
                link_data: {
                    image_hash: values.image_hash,
                    link: values.link,
                    message: values.message
                }
            }
        }
        createAdCreative(data).finally(() => {
            props.adCreativeData();
        });
    };
    return (
        <>
            <Form
                {...layout}
                initialValues={{ name:  "Gucci AdCreative for Link Ad.", page_id: "104413048775500",
                    image_hash: "4f9914935a345227409b2cc7f811928c", link: "https://www.ounass.ae/designers/gucci",
                    message: "try it out"
                }}
                ref={formRef}
                name="control-ref"
                onFinish={onFinish}
                style={{
                    maxWidth: 600,
                }}
            >
                <Form.Item
                    name="name"
                    label="Name"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input type={"text"} key="name"/>
                </Form.Item>
                <Form.Item
                    name="page_id"
                    label="Page Id"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input type={"text"} key="page_id"/>
                </Form.Item>
                <Form.Item
                    name="image_hash"
                    label="Image Hash"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input type={"text"} key="image_hash"/>
                </Form.Item>
                <Form.Item
                    name="link"
                    label="Link"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input type={"text"} key="link"/>
                </Form.Item>
                <Form.Item
                    name="message"
                    label="Message"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input type={"text"} key="message"/>
                </Form.Item>
                <Form.Item {...tailLayout}>
                    <Button type="primary" htmlType="submit">
                        Submit
                    </Button>
                </Form.Item>
            </Form>
        </>
    );
};
export default AddAdCreativeForm;
