from langchain.embeddings import HuggingFaceInstructEmbeddings
from sentence_transformers import SentenceTransformer, util
import torch
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from transformers import LlamaTokenizer, LlamaForCausalLM, AutoModelForCausalLM, AutoModel, AutoTokenizer

class SimilarityEmbeddings:

    def load_instructor_model(self,model_name, device='cpu'):
        instructor_embeddings = HuggingFaceInstructEmbeddings(model_name=model_name,
                                                              model_kwargs={"device": device})

        return instructor_embeddings

    def sentence_transformers_model(self,model_name, device='cpu',max_seq_length = 512,normalize_embeddings=False):
        model = SentenceTransformer(model_name,device=device,
                                    encode_kwargs={'normalize_embeddings': normalize_embeddings})
        model.max_seq_length = max_seq_length

        return model

class LLM:

    def load_os_llm(self, model_name, load_in_4bit=False, load_in_8bit=False, device_map='cpu',
                low_cpu_mem_usage=False,torch_dtype=torch.float32, trust_remote_code=True,
                quantization_config=None):

        try:
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                load_in_4bit=load_in_4bit,
                load_in_8bit=load_in_8bit,
                device_map=device_map,
                low_cpu_mem_usage=low_cpu_mem_usage,
                trust_remote_code=trust_remote_code,
                torch_dtype=torch_dtype,
                quantization_config=quantization_config
            )
        except NameError:
            try:

                model = AutoModel.from_pretrained(
                    model_name,
                    load_in_4bit=load_in_4bit,
                    load_in_8bit=load_in_8bit,
                    device_map=device_map,
                    low_cpu_mem_usage=low_cpu_mem_usage,
                    trust_remote_code=trust_remote_code,
                    torch_dtype=torch_dtype,
                    quantization_config=quantization_config
                )
            except:
                model = LlamaForCausalLM.from_pretrained(model_name,
                    load_in_4bit=load_in_4bit,
                    load_in_8bit=load_in_8bit,
                    device_map=device_map,
                    low_cpu_mem_usage=low_cpu_mem_usage,
                    trust_remote_code=trust_remote_code,
                    torch_dtype=torch_dtype,
                    quantization_config=quantization_config
                )
        return model

    def load_llm_tokenizer(self, model_name,use_fast_tokenizer=True):
        try:
            tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                use_fast=use_fast_tokenizer
            )
        except TypeError:
            tokenizer = AutoTokenizer.from_pretrained(
                model_name, use_fast=False
            )

        return tokenizer

    def load_pipeline_hf(self,task,model,tokenizer,max_length,temperature,top_p,repetition_penalty):

        pipe = pipeline(
            task,
            model=model,
            tokenizer=tokenizer,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            repetition_penalty=repetition_penalty
        )

        local_llm = HuggingFacePipeline(pipeline=pipe)

        return local_llm


