import {Modal} from 'antd';
import React from 'react';

const DialogWithFooter = (props) => {
    return (
        <>
            <Modal
                width={props.width}
                title={props.title}
                open={props.visible}
                onOk={props.onOk}
                onCancel={props.onCancel}
            >
                {props.children}
            </Modal>
        </>
    );
};
export default DialogWithFooter;
