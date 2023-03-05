import {Button, Divider, Form, Input, Select} from 'antd';
import React from 'react';
import {createAdset} from "../../../services/services";

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
const AddAdsetForm = (props) => {
    const formRef = React.useRef(null);

    const onFinish = (values) => {
        props.setVisible(false);
        let data = {
            name: values.name,
            daily_budget: values.daily_budget,
            bid_amount: values.bid_amount,
            targeting: {
                age_min: values.age_min,
                age_max: values.age_max,
                geo_locations: {
                    countries: values.countries,
                }
            },
            campaign_id: values.campaign_id,
            billing_event: values.billing_event,
            optimization_goal: values.optimization_goal
        }
        createAdset(data).finally(() => {
            props.adsetData();
        });
    };
    return (
        <Form
            {...layout}
            initialValues={{ name: "My first Adset Abdurrahman Pektas", daily_budget: 2000, campaign_id: props.campaign_id,
                ends_after: 10, bid_amount: 5, billing_event: "IMPRESSIONS", optimization_goal: "REACH",
                age_min: 20, age_max: 35, countries: ["AE", "SA", "KW"]
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
                name="daily_budget"
                label="Daily Budget"
                rules={[
                    {
                        required: true,
                    },
                ]}
            >
                <Input type={"number"} key="daily_budget"/>
            </Form.Item>
            <Form.Item
                name="campaign_id"
                label="Campaign Id"
                rules={[
                    {
                        required: true,
                    },
                ]}
            >
                <Input disabled={true} type={"text"} key="campaign_id"/>
            </Form.Item>
            <Form.Item
                name="ends_after"
                label="Duration (days)"
                rules={[
                    {
                        required: true,
                    },
                ]}
            >
                <Input type={"number"} key="ends_after"/>
            </Form.Item>
            <Form.Item
                name="bid_amount"
                label="Bid Amount"
                rules={[
                    {
                        required: true,
                    },
                ]}
            >
                <Input type={"number"} key="bid_amount"/>
            </Form.Item>
            <Form.Item
                name="billing_event"
                label="Billing Event"
                rules={[
                    {
                        required: true,
                    },
                ]}
            >
                <Input type={"text"} key="billing_event"/>
            </Form.Item>
            <Form.Item
                name="optimization_goal"
                label="Optimization Goal"
                rules={[
                    {
                        required: true,
                    },
                ]}
            >
                <Input type={"text"} key="optimization_goal"/>
            </Form.Item>
            <Divider orientation="left">Target</Divider>
            <Form.Item
                name="age_min"
                label="Min Age"
                rules={[
                    {
                        required: true,
                    },
                ]}
            >
                <Input type={"number"} key="age_min"/>
            </Form.Item>
            <Form.Item
                name="age_max"
                label="Max Age"
                rules={[
                    {
                        required: true,
                    },
                ]}
            >
                <Input type={"number"} key="age_max"/>
            </Form.Item>
            <Form.Item
                name="countries"
                label="Countries"
                rules={[
                    {
                        required: true,
                    },
                ]}
            >
                <Select
                    mode="multiple"
                    allowClear
                    style={{
                        width: '100%',
                    }}
                    placeholder="Please select"
                    options={["AE", "SA", "KW"].map(country => {return {value: country, label: country}})}
                />
            </Form.Item>
            <Form.Item {...tailLayout}>
                <Button type="primary" htmlType="submit">
                    Submit
                </Button>
            </Form.Item>
        </Form>
    );
};
export default AddAdsetForm;
