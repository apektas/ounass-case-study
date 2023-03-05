import {Button, Form, Input} from 'antd';
import React from 'react';
import {createCampaign} from "../../../services/services";


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

const AddCampaignForm = (props) => {
    const formRef = React.useRef(null);

    const onFinish = (values) => {
        props.setVisible(false);
        createCampaign(values).finally(() => {
            props.campaignData();
        });
    };
    return (
        <>
            <Form
                {...layout}
                initialValues={{ name: "Conversions Campaign Abdurrahman Pektas", objective: "REACH"}}
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
                    name="objective"
                    label="Objective"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input type={"text"} key="objective"/>
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
export default AddCampaignForm;
