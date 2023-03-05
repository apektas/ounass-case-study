import {Modal} from 'antd';
import React from 'react';

const DialogWithNoFooter = (props) => {
    return (
        <>
            <Modal
                title={props.title}
                open={props.visible}
                onOk={props.onOk}
                onCancel={props.onCancel}
                footer={[]}
            >
                {props.children}
            </Modal>
        </>
    );
};
export default DialogWithNoFooter;
