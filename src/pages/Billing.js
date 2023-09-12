import React, { useState, useEffect } from "react";
import {
  Row,
  Col,
  Card,
  Table,
  Button,
  Radio,
  Typography,
  DatePicker,
} from "antd";
import moment from "moment";

const { Text } = Typography;

const dataSource = [
  {
    nama: "Adam Ramdani Yunus",
    jadwal: "Monday",
    status: null,
  },
  {
    nama: "Abisena Putra",
    jadwal: "Tuesday",
    status: null,
  },
  {
    nama: "Djalu Galang",
    jadwal: "Friday",
    status: null,
  },
  {
    nama: "Keiwa Sakurai",
    jadwal: "Thursday",
    status: null,
  },
];

function Billing() {
  const [filteredDataSource, setFilteredDataSource] = useState([]);
  const [selectedDate, setSelectedDate] = useState(moment().format("YYYY-MM-DD"));

  const handleButtonClick = (record) => {
    // Lakukan sesuatu ketika tombol hijau ditekan
    console.log("Tombol hijau ditekan untuk", record.nama);
  };

  useEffect(() => {
    // Otomatis mengatur tanggal awal saat komponen dimuat
    handleDateChange(moment().format("YYYY-MM-DD"));
  }, []);

  const handleDateChange = (dateString) => {
    // Lakukan sesuatu ketika tanggal dipilih
    console.log("Tanggal yang dipilih:", dateString);
    setSelectedDate(dateString);
  };

  useEffect(() => {
    // Mengonversi tanggal yang dipilih menjadi hari dalam bahasa Inggris
    const selectedDay = moment(selectedDate).format("dddd");

    // Memfilter data berdasarkan hari yang dipilih
    const filteredData = dataSource.filter((item) => item.jadwal === selectedDay);
    
    // Periksa apakah ada data untuk hari yang dipilih
    if (filteredData.length > 0) {
      setFilteredDataSource(filteredData);
    } else {
      // Jika tidak ada data, kosongkan filteredDataSource
      setFilteredDataSource([]);
    }
  }, [selectedDate]);

  const columns = [
    {
      title: "Nama",
      dataIndex: "nama",
      key: "nama",
    },
    {
      title: "Jadwal",
      dataIndex: "jadwal",
      key: "jadwal",
    },
    {
      title: "Status",
      dataIndex: "status",
      key: "status",
      render: (status, record) => (
        <>
          <Radio.Group buttonStyle="solid">
            <Radio.Button value="Sakit">Sakit</Radio.Button>
            <Radio.Button value="Hadir">Hadir</Radio.Button>
            <Radio.Button value="Alpha">Alpha</Radio.Button>
          </Radio.Group>
        </>
      ),
    },
    
    {
      title: "Action",
      key: "action",
      render: (text, record) => (
        <Button
          type="primary"
          onClick={() => handleButtonClick(record)}
          style={{ backgroundColor: "green", borderColor: "green" }}
        >
          Submit
        </Button>
      ),
    },
  ];

  return (
    <Row gutter={[16, 16]}>
      <Col span={24}>
        <Card title="Absensi Piket">
          <div>
            <DatePicker
              value={moment(selectedDate)}
              onChange={(date, dateString) => handleDateChange(dateString)}
            />
          </div>
          {selectedDate && (
            <Text>
              Tanggal yang dipilih: {moment(selectedDate).format("DD MMMM YYYY")}
            </Text>
          )}
          <Table
            dataSource={filteredDataSource}
            columns={columns}
            pagination={{
              pageSize: 7,
            }}
          />
        </Card>
      </Col>
    </Row>
  );
}

export default Billing;
