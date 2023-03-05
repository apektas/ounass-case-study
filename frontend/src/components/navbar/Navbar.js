import {Layout, Menu} from 'antd';
import React, {useState} from "react";
import { useNavigate } from "react-router-dom";
import {navbarItems} from "../../utils/Constants"
const { Header} = Layout;
const Navbar = (props) => {
    const navigate = useNavigate();
    const [current, setCurrent] = useState('campaign');
    const menuOnClick = (e) => {
        setCurrent(e.key);
        navigate(navbarItems.find(item => item.key === e.key).url || "/");
    };

    return (
            <Header
                style={{
                    position: 'sticky',
                    top: 0,
                    zIndex: 1,
                    width: '100%'
                }}
            >
                <div style={{
                    float: "left",
                    width: "250px",
                    height: "50px",
                    margin: "5px 50px",
                    background: "white"
                }}>
                    <img src={"/assets/logo.png"}  width="200px" height="50px"  />
                </div>
                <Menu
                    theme="dark"
                    mode="horizontal"
                    defaultSelectedKeys={current}
                    items={navbarItems}
                    onClick={menuOnClick}
                />
            </Header>
    );
};
export default Navbar;
