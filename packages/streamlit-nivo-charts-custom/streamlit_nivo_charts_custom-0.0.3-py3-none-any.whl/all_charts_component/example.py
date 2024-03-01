import streamlit as st
from __init__ import chart_to_display

data_ = [
  {
    "id": "java",
    # "label": "java",
    "value": 214,
    "color": "hsl(330, 70%, 50%)"
  },
  {
    "id": "javascript",
    # "label": "javascript",
    "value": 395,
    "color": "hsl(207, 70%, 50%)"
  },
  {
    "id": "make",
    # "label": "make",
    "value": 147,
    "color": "hsl(332, 70%, 50%)"
  },
  {
    "id": "css",
    # "label": "css",
    "value": 291,
    "color": "hsl(136, 70%, 50%)"
  },
  {
    "id": "php",
    # "label": "php",
    "value": 558,
    "color": "hsl(147, 70%, 50%)"
  }
]

chartLayout = {
    "margin":{ "top": 40, "right": 80, "bottom": 80, "left": 80 },
    "innerRadius":0.5,
    "padAngle":0.7,
    "cornerRadius":3,
    "activeOuterRadiusOffset":8,
    "borderWidth":1,
    "borderColor":{
            "from": 'color',
            "modifiers": [
                [
                    'darker',
                    0.2
                ]
            ]
        },
    "arcLinkLabelsSkipAngle":10,
    "arcLinkLabelsTextColor":"#333333",
    "arcLinkLabelsThickness":2,
    "arcLinkLabelsColor":{ "from": 'color' },
    "arcLabelsSkipAngle":10,
    "legends":[
            {
                "anchor": 'bottom',
                "direction": 'row',
                "justify": False,
                "translateX": 0,
                "translateY": 56,
                "itemsSpacing": 0,
                "itemWidth": 100,
                "itemHeight": 18,
                "itemTextColor": '#999',
                "itemDirection": 'left-to-right',
                "itemOpacity": 1,
                "symbolSize": 18,
                "symbolShape": 'circle',
                "effects": [
                    {
                        "on": 'hover',
                        "style": {
                            "itemTextColor": '#000'
                        }
                    }
                ]
            }
        ]
}

with st.columns([1,10,1])[1]:
    chart_to_display(chartData=data_, chartLayout=chartLayout)

funnel_chart_ = [
  {
    "id": "step_sent",
    "value": 70624,
    "label": "Sent"
  },
  {
    "id": "step_viewed",
    "value": 51512,
    "label": "Viewed"
  },
  {
    "id": "step_clicked",
    "value": 48753,
    "label": "Clicked"
  },
  {
    "id": "step_add_to_card",
    "value": 30771,
    "label": "Add To Card"
  },
  {
    "id": "step_purchased",
    "value": 24226,
    "label": "Purchased"
  }
]
funnel_layout_c = {
    "margin":{ "top": 20, "right": 20, "bottom": 20, "left": 20 },
        "valueFormat":">-.4s",
        "enableLabel":True,
        "isInteractive":True,
        "colors":{ "scheme": 'spectral' },
        "borderWidth":20,
        "labelColor":{
            "from": 'color',
            "modifiers": [
                [
                    'darker',
                    3
                ]
            ]
        },
        "beforeSeparatorLength":100,
        "beforeSeparatorOffset":20,
        "afterSeparatorLength":100,
        "afterSeparatorOffset":20,
        "currentPartSizeExtension":10,
        "currentBorderWidth":40,
        "motionConfig":"wobbly"
}

with st.columns([1,10,1])[1]:
    chart_to_display(chartType="funnelChart", chartData=funnel_chart_, chartLayout=funnel_layout_c)

circle_chart = {
  "name": "nivo",
  "color": "hsl(127, 70%, 50%)",
  "children": [ 
      {
        "name": "viz",
        "value":500
      },
      {
        "name": "Dannie",
        "value":100
      }
  ]
}

circle_Chart_layout = {
    "margin":{ "top": 20, "right": 20, "bottom": 20, "left": 20 },
    "id":"name",
    "value":"value",
    "colors":{ "scheme": 'nivo' },
    "childColor":{
        "from": 'color',
        "modifiers": [
            [
                'brighter',
                0.4
            ]
        ]
    },
    "padding":4,
    "enableLabels":True,
    # "labelsFilter": "n=>2===n.node.depth",
    "labelsSkipRadius":10,
    "labelTextColor":{
        "from": 'color',
        "modifiers": [
            [
                'darker',
                2
            ]
        ]
    },
    "borderWidth":1,
    "borderColor":{
        "from": 'color',
        "modifiers": [
            [
                'darker',
                0.5
            ]
        ]
    }
}

with st.columns([1,10,1])[1]:
    chart_to_display(chartType="circlePacking", chartData=circle_chart, chartLayout=circle_Chart_layout)

