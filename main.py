import tkinter as tk
import re
from pypinyin import lazy_pinyin


def hanzi_to_pinyin():
    """
    处理按钮点击事件：获取文本、转换拼音、输出结果
    """
    raw_text = input_text.get("1.0", tk.END)

    # 正则清理：删除标点符号和换行符，只保留汉字、字母和数字
    clean_text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', raw_text)

    if not clean_text:
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.config(state=tk.DISABLED)
        return

    pinyin_list = lazy_pinyin(clean_text)
    result = ' '.join(pinyin_list)

    # 将结果显示在输出框中
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state=tk.DISABLED)


def clear_text():
    """
    清空输入框和输出框
    """
    input_text.delete("1.0", tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)


def copy_result():
    """
    将输出框的内容复制到系统剪贴板，并提供视觉反馈
    """
    # 获取输出框中的文本内容（去掉末尾多余的换行符）
    result_text = output_text.get("1.0", tk.END).strip()

    if result_text:
        # 清空剪贴板并写入新内容
        root.clipboard_clear()
        root.clipboard_append(result_text)
        root.update()  # 确保剪贴板更新

        # 视觉反馈：改变按钮文字
        copy_btn.config(text="✅ 复制成功！", fg="green")
        # 2000毫秒（2秒）后恢复按钮原来的文字
        root.after(2000, reset_copy_button)


def reset_copy_button():
    """
    恢复复制按钮的默认状态
    """
    copy_btn.config(text="📋 复制结果", fg="black")


# ================= 界面构建部分 =================

root = tk.Tk()
root.title("PurePinyin 极简拼音转换器")
# 稍微加宽一点窗口，以容纳三个按钮
root.geometry("650x500")
root.configure(padx=20, pady=20)

# --- 输入区 ---
input_label = tk.Label(root, text="👇 请在此粘贴或输入需要转换的文字（支持多行）：", font=("微软雅黑", 10))
input_label.pack(anchor="w", pady=(0, 5))

input_text = tk.Text(root, height=8, font=("微软雅黑", 11))
input_text.pack(fill=tk.BOTH, expand=True)

# --- 按钮区 ---
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

convert_btn = tk.Button(button_frame, text="🚀 开始转换", font=("微软雅黑", 12, "bold"),
                        bg="#4CAF50", fg="white", activebackground="#45a049",
                        command=hanzi_to_pinyin, width=12, height=1)
convert_btn.pack(side=tk.LEFT, padx=10)

copy_btn = tk.Button(button_frame, text="📋 复制结果", font=("微软雅黑", 12),
                     command=copy_result, width=12, height=1)
copy_btn.pack(side=tk.LEFT, padx=10)

clear_btn = tk.Button(button_frame, text="🗑️ 清空内容", font=("微软雅黑", 12),
                      command=clear_text, width=12, height=1)
clear_btn.pack(side=tk.LEFT, padx=10)

# --- 输出区 ---
output_label = tk.Label(root, text="✨ 转换结果（已自动删除标点与换行，用空格分隔）：", font=("微软雅黑", 10))
output_label.pack(anchor="w", pady=(0, 5))

output_text = tk.Text(root, height=8, font=("微软雅黑", 11), bg="#f5f5f5")
output_text.pack(fill=tk.BOTH, expand=True)
output_text.config(state=tk.DISABLED)

# 运行主循环
root.mainloop()