# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .context_dto import ContextDTO


class QnASearchResultContext(ContextDTO):
    """Context object of the QnA.

    :param is_context_only: To mark if a prompt is relevant only with a
     previous question or not.
     true - Do not include this QnA as search result for queries without
     context
     false - ignores context and includes this QnA in search result
    :type is_context_only: bool
    :param prompts: List of prompts associated with the answer.
    :type prompts:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.PromptDTO]
    """

    _validation = {
        'prompts': {'max_items': 20},
    }

    _attribute_map = {
        'is_context_only': {'key': 'isContextOnly', 'type': 'bool'},
        'prompts': {'key': 'prompts', 'type': '[PromptDTO]'},
    }

    def __init__(self, **kwargs):
        super(QnASearchResultContext, self).__init__(**kwargs)
