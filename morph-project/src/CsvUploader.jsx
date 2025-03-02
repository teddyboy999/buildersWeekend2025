import { useState } from 'react';
import Papa from 'papaparse';
import { supabase } from './supabaseClient';

const CsvUploader = ({ onDataLoaded }) => {
  const [data, setData] = useState([]);
  const [status, setStatus] = useState('');

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) {
      setStatus('No file selected');
      return;
    }

    Papa.parse(file, {
      header: true,
      skipEmptyLines: true,
      complete: async (result) => {
        const expectedColumns = ['product_id', ...Array.from({ length: 30 }, (_, i) => `day${i + 1}`)];
        if (!expectedColumns.every(col => col in result.data[0])) {
          setStatus('CSV must have product_id, day1, ..., day30');
          return;
        }

        const formattedData = result.data.map(row => ({
          product_id: row.product_id,
          ...Object.fromEntries(
            Array.from({ length: 30 }, (_, i) => [`day${i + 1}`, parseInt(row[`day${i + 1}`]) || 0])
          ),
        }));

        setData(formattedData);
        setStatus('File loaded — uploading to Supabase...');

        try {
          const { error } = await supabase
            .from('stock_data')
            .insert(formattedData);

          if (error) throw error;
          setStatus('File uploaded to Supabase');
          onDataLoaded(formattedData); // Pass data to parent
        } catch (error) {
          setStatus(`Error uploading: ${error.message}`);
          console.error('Upload error:', error);
        }
      },
      error: (error) => {
        setStatus(`Parse error: ${error.message}`);
      },
    });
  };

  return (
    <div className="p-4 border rounded-lg shadow-md">
      <input
        type="file"
        accept=".csv"
        onChange={handleFileUpload}
        className="mb-4"
      />
      {status && <p className="mb-4">{status}</p>}
      {data.length > 0 && (
        <table className="border-collapse border border-gray-400 w-full">
          <thead>
            <tr>
              {Object.keys(data[0]).map((key) => (
                <th key={key} className="border border-gray-300 p-2">
                  {key}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, index) => (
              <tr key={index}>
                {Object.values(row).map((value, idx) => (
                  <td key={idx} className="border border-gray-300 p-2">
                    {value}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default CsvUploader;