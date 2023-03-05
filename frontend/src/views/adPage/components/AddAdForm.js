import {Button, Form, Input, Select} from 'antd';
import React, {useEffect, useState} from 'react';
import {createAd, getAdCreatives} from "../../../services/services";


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

const AddAdForm = (props) => {
    const formRef = React.useRef(null);
    const [adCreatives, setAdCreatives] = useState([]);

    useEffect(() => {
        getAdCreatives().then((response) => {
            if(response?.data !== null) {
                setAdCreatives(response.data);
            }
            return response;
        });
    }, []);

    const onFinish = (values) => {
        props.setVisible(false);
        let data = {
            name: values.name,
            adset_id: values.adset_id,
            creative: {
                creative_id: values.creative_id
            },
            status: values.status
        }
        createAd(data).finally(() => {
            props.adData();
        });
    };
    return (
        <>
            <Form
                {...layout}
                initialValues={{ name:  "My Ad Abdurrahman Pektas", adset_id: props.adset_id  ,status: "PAUSED"}}
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
                    name="adset_id"
                    label="Adset Id"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input disabled={true} type={"text"} key="adset_id"/>
                </Form.Item>
                <Form.Item
                    name="creative_id"
                    label="AdCreative ID"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Select
                        key="creative_id"
                        showSearch
                        placeholder="Select an adCreativeId"
                        optionFilterProp="children"
                        filterOption={(input, option) =>
                            (option?.label ?? '').toLowerCase().includes(input.toLowerCase())
                        }
                        options={adCreatives?.map(adCreative => {
                            return {
                                value: adCreative.id,
                                label: adCreative.label
                            }
                        })}
                    />
                </Form.Item>
                <Form.Item
                    name="status"
                    label="Status"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input type={"text"} key="status"/>
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
export default AddAdForm;
